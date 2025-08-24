# CRM Platform

CRM platform made in Django where you can generate data of 500K rows in a PostgreSQL database and explore them in the platform itself.
It uses Django, PostgreSQL, and Bootstrap (Minty theme from Bootswatch) for a clean and modern interface.

---

## Features
- Generate ~500K rows of demo data (Users, Companies, Customers, Interactions).
- Explore customers with:
  - Full name
  - Company
  - Birthday
  - Last interaction (date and type, e.g. `1 day ago (Phone)`).
- Filtering by name or birthday (e.g. birthdays this week).
- Ordering by name, company, birthday, or last interaction.
- Pagination for large datasets.
- Production-ready Docker setup with Gunicorn + PostgreSQL.

## Local Installation

### 1. Clone the repository
```bash
git clone https://github.com/robertcharca/tip-crm-platform.git
cd crm-platform
```

### 1.1. Reminder
Make sure to create a `.env` file with the following variables:
```text
POSTGRES_DB=crm-platform
POSTGRES_USER=root
POSTGRES_PASSWORD=1234
POSTGRES_HOST=postgres

DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=0
```


### 2. Build and start services
```bash
docker compose up --build -d
```

### 2.1. Database setup
Apply migrations inside the container:
```bash
docker compose exec web python manage.py migrate
```

### 2.2. Data generation (500K rows)
This project includes a custom Django command to generate large amounts of fake CRM data. It will populate:
- Users: 3
- Companies: 10
- Customers: 1000
- Interactions: 500 per customer, which is 500,000 rows total

Run the seeding command:
```bash
docker compose exec web python manage.py seed_initial_data
```

### 3. Accessing the CRM
Go to: http://127.0.0.1:8000

### 4. Useful commands
View logs of the web service:
```bash
docker compose logs -f web
```

Enter Django shell:
```bash
docker compose exec web python manage.py shell
```