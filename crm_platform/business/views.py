from django.shortcuts import render
from django.db.models import Max, F, Q
from django.utils.timezone import now
from datetime import timedelta
from django.core.paginator import Paginator
from business.models import Customers, Interactions

def customer_list(request):
    """
    customer_list: view that list customers data.

    1. Fetches all customers with their related company and user using 
    `select_related`, then annotates each customer with their most 
    recent interaction date and type.
    
    2. Allows filtering: users can search by customer name or last name, 
    and optionally filter customers whose birthday falls within the 
    current week.
    
    3. Supports dynamic ordering: results can be sorted by customer name, 
    company, birthday, or latest interaction date.
    
    4. Implements pagination: results are split into pages of 25 customers 
    each, making large datasets easier to navigate.
    """

    customers = Customers.objects.all().select_related("company", "user")

    # Annotate with last interaction
    customers = customers.annotate(
        last_interaction_date=Max("interactions__interaction_date"),
        last_interaction_type=F("interactions__interaction_type"),
    )

    # Filtering
    search = request.GET.get("search")
    if search:
        customers = customers.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search)
        )

    birthday = request.GET.get("birthday")
    if birthday == "this_week":
        today = now().date()
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        customers = customers.filter(birthdate__range=[start_week, end_week])

    # Ordering
    order = request.GET.get("order")
    if order == "name":
        customers = customers.order_by("first_name", "last_name")
    elif order == "company":
        customers = customers.order_by("company_id__name")
    elif order == "birthday":
        customers = customers.order_by("birthdate")
    elif order == "last_interaction":
        customers = customers.order_by("-last_interaction_date")

    # Pagination
    paginator = Paginator(customers, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "crm/customer_list.html", {"page_obj": page_obj})