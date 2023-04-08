"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# connect to db
conn = psycopg2.connect(host='localhost', port=5433, database='north', user='postgres', password='12345')
try:
    with conn:
        cur = conn.cursor()
        # работники (employees)
        with open('north_data/employees_data.csv') as file:
            data = [tuple(line) for line in csv.reader(file)]  # список кортежей
            for item in range(1, len(data)):
                # execute query
                cur.execute("INSERT INTO employees VALUES (default, %s, %s, %s, %s, %s)", data[item])
        # покупатели (customers)
        with open('north_data/customers_data.csv') as file:
            data = [tuple(line) for line in csv.reader(file)]  # список кортежей
            for item in range(1, len(data)):
                # execute query
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", data[item])
        # заказы (orders)
        with open('north_data/orders_data.csv') as file:
            data = [tuple(line) for line in csv.reader(file)]  # список кортежей
            for item in range(1, len(data)):
                # execute query
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", data[item])
finally:
    conn.close()


# conn = psycopg2.connect(host='localhost', port=5433, database='north', user='postgres', password='12345')
# try:
#     with conn:
#         with conn.cursor as cur:
#             with open('north_data/employees_data.csv') as file:
#                 data = [tuple(line) for line in csv.reader(file)]  # список кортежей
#                 for item in range(1, len(data)):
#                     # execute query
#                     cur.execute("INSERT TO employees VALUES (%s, %s, %s, %s, %s)", data[item])
# finally:
#     conn.close()
