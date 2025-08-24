# CRM Platform: Details

## E/R Diagram
The Entity-Relationship diagram is based with the following fields:

### Users
- **user_id:** primary key for Users.
- **name:** representative name.
- **email:** representative email.
- **password:** representative password.
- **admin:** admin validation for representative.
- **created_at:** creation date.
- **updated_at:** update date.
### Companies
- **company_id:** primary key for Companies.
- **name:** company name.
- **created_at:** creation date.
- **updated_at:** update date.
### Customers
- **customer_id:** primary key for Customers.
- **first_name:** customer's first name.
- **last_name:** customer's last name.
- **birthdate:** customer's birth-date.
- **company_id:** foreign key for company id.
- **user_id:** foreign key for user id.
- **created_at:** creation date.
- **updated_at:** update date.
### Interactions
- **interaction_id:** primary key for Interactions.
- **customer_id:** foreign key for customer id.
- **interaction_type:** type of given interaction.
- **interaction_date:** date of given interaction

## Possible Initial AWS Architecture
Due to the way this project is implemented, it's possible to implement an initial architecture in AWS with ECS, RDS and networking services as well as logs and secrets services.