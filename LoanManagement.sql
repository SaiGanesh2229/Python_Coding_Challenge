create database LoanManagement;
use LoanManagement;
-- 1. Table for Customer
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    address VARCHAR(255),
    credit_score INT
);

-- 2. Table for Loans
CREATE TABLE Loan (
    loan_id INT PRIMARY KEY,
    customer_id INT,
    principal_amount DECIMAL(15, 2),
    interest_rate DECIMAL(5, 2),
    loan_term INT,
    loan_type VARCHAR(50),
    loan_status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

select * from Customer;
