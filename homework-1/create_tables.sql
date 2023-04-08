-- SQL-команды для создания таблиц
DROP TABLE IF EXISTS orders, employees, customers;

CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name char(30) NOT NULL,
	last_name char(30) NOT NULL,
	title char(100) NOT NULL,
	birst_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
	company_name char(50) NOT NULL,
	contact_name char(50) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5),
	FOREIGN KEY(customer_id)
	REFERENCES customers(customer_id),
	employee_id serial,
	FOREIGN KEY(employee_id)
	REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_city char(30) NOT NULL
);

SELECT * FROM orders;
SELECT * FROM employees;
SELECT * FROM customers;
