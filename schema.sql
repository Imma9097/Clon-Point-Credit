-- Clients Table
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    id_number VARCHAR(50) UNIQUE NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    residence VARCHAR(100),
    business_type VARCHAR(100),
    business_location VARCHAR(100)
);

-- Loans Table
CREATE TABLE Loans (
    loan_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    loan_amount DECIMAL(10, 2) NOT NULL,
    interest_rate DECIMAL(5, 2) DEFAULT 8.00,
    appraisal_fee DECIMAL(10, 2) DEFAULT 300.00,
    start_date DATE NOT NULL,
    due_date DATE NOT NULL,
    principal_balance DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);

-- Payments Table
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,
    loan_id INT NOT NULL,
    payment_date DATE NOT NULL,
    amount_paid DECIMAL(10, 2) NOT NULL,
    payment_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (loan_id) REFERENCES Loans(loan_id)
);

-- Penalties Table
CREATE TABLE Penalties (
    penalty_id SERIAL PRIMARY KEY,
    loan_id INT NOT NULL,
    penalty_amount DECIMAL(10, 2) NOT NULL,
    penalty_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    FOREIGN KEY (loan_id) REFERENCES Loans(loan_id)
);

-- Reports Table
CREATE TABLE Reports (
    report_id SERIAL PRIMARY KEY,
    report_type VARCHAR(50) NOT NULL,
    report_date DATE NOT NULL,
    data TEXT NOT NULL
);