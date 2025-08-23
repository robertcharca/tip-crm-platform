-- Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    admin BOOLEAN DEFAULT FALSE,
    created_at DATE DEFAULT CURRENT_DATE,
    updated_at DATE DEFAULT CURRENT_DATE
);

-- Companies table
CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE,
    updated_at DATE DEFAULT CURRENT_DATE
);

-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    birthdate DATE NOT NULL,
    company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE SET NULL,
    created_at DATE DEFAULT CURRENT_DATE,
    updated_at DATE DEFAULT CURRENT_DATE
);

-- Interactions table
CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE,
    interaction_type VARCHAR(50) NOT NULL CHECK (interaction_type IN ('Call', 'Email', 'SMS', 'Facebook', 'WhatsApp', 'Other')),
    interaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Insert users data
INSERT INTO users (name, email, password, admin)
VALUES 
('Alice Rodríguez', 'alice@example.com', 'password123', TRUE),
('Bruno García', 'bruno@example.com', 'password123', FALSE),
('Carla Fernández', 'carla@example.com', 'password123', FALSE);

-- Insert companies data
INSERT INTO companies (name)
VALUES
('Tech Solutions S.A.'),
('Innovatech Perú'),
('DataCorp'),
('Green Energy Ltd.'),
('Global Logistics Inc.'),
('HealthPlus Clinic'),
('EduSmart Academy'),
('Finanzas Seguras'),
('TravelWorld Agency'),
('Construcciones Modernas S.A.');