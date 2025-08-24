from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
import random
from tqdm import tqdm
from business.models import Users, Companies, Customers, Interactions
from django.utils import timezone


fake = Faker("es_ES")


class Command(BaseCommand):
    help = "Seed initial Users and Companies"


    def handle(self, *args, **kwargs):
        if not Users.objects.exists():
            self.stdout.write("Creating Users data...")
            users = [
                {"name": "Alice Rodríguez", "email": "alice@example.com", "admin": True},
                {"name": "Bruno García", "email": "bruno@example.com", "admin": False},
                {"name": "Carla Fernández", "email": "carla@example.com", "admin": False},
            ]
            for u in users:
                Users.objects.get_or_create(
                    email=u["email"],
                    defaults={
                        "name": u["name"],
                        "password": make_password("password123"),
                        "admin": u["admin"],
                    },
                )
        else:
            self.stdout.write(self.style.WARNING("Users table already has data"))

        if not Companies.objects.exists():
            self.stdout.write("Creating Companies data...")
            companies = [
                "Tech Solutions S.A.",
                "Innovatech Perú",
                "DataCorp",
                "Green Energy Ltd.",
                "Global Logistics Inc.",
                "HealthPlus Clinic",
                "EduSmart Academy",
                "Finanzas Seguras",
                "TravelWorld Agency",
                "Construcciones Modernas S.A.",
            ]
            for name in companies:
                Companies.objects.get_or_create(name=name)
        else:
            self.stdout.write(self.style.WARNING("Companies table already has data"))

        if not Customers.objects.exists():
            self.stdout.write("Creating Customers data...")

            companies = list(Companies.objects.all())
            users = list(Users.objects.all())

            customers = []
            for _ in tqdm(range(1000)):
                company = random.choice(companies)
                user = random.choice(users)
                customers.append(
                    Customers(
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        birthdate=fake.date_of_birth(minimum_age=18, maximum_age=70),
                        company=company,
                        user=user,
                    )
                )
            Customers.objects.bulk_create(customers, batch_size=500)
        else:
            self.stdout.write(self.style.WARNING("Customers table already has data"))

        if not Interactions.objects.exists():
            self.stdout.write("Creating Interactions data...")
            interaction_types = ["Call", "Email", "SMS", "Facebook", "WhatsApp", "Other"]

            all_customers = list(Customers.objects.all())
            interactions = []
            for customer in tqdm(all_customers):
                for _ in range(500):
                    interactions.append(
                        Interactions(
                            customer=customer,
                            interaction_type=random.choice(interaction_types),
                            interaction_date=fake.date_time_this_decade(tzinfo=timezone.get_current_timezone()),
                        )
                    )
                if len(interactions) > 10000:
                    Interactions.objects.bulk_create(interactions, batch_size=5000)
                    interactions = []

            if interactions:
                Interactions.objects.bulk_create(interactions, batch_size=5000)
        else:
            self.stdout.write(self.style.WARNING("Interactions table already has data"))

        self.stdout.write(self.style.SUCCESS(f"\nData seeding processed ended successfully. \nUsers: {Users.objects.count()}, Companies: {Companies.objects.count()}, Customers: {Customers.objects.count()}, Interactions: {Interactions.objects.count()}"))