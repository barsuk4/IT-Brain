import os
import psycopg2
from faker import Faker
import random
from datetime import date
from datetime import timedelta

class DatabaseManager:
    def __init__(self, host, port, dbname, user, password):
        self.conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

class Users:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                email VARCHAR(100) UNIQUE NOT NULL,
                registered_date DATE NOT NULL,
                date_of_birth DATE NOT NULL,
                address VARCHAR(255)
            );
        """)

    def insert_sample_data(self):
        fake = Faker('uk_UA')
        for i in range(10000):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = str(i) + fake.email()
            registered_date = date.today() - timedelta(days=i)
            date_of_birth = date.today() - timedelta(days=(365 * (random.randint(3, 10) * 6)))  # Birth dates within the last 60 years
            address = fake.address().replace("\n", ", ")

            self.db.cursor.execute("""
                INSERT INTO users (first_name, last_name, email, registered_date, date_of_birth, address)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (first_name, last_name, email, registered_date, date_of_birth, address))

# Аналогічно створюємо класи для інших таблиць...
class Books:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                publish_date DATE,
                isbn VARCHAR(255) UNIQUE NOT NULL
            );
        """)

    def insert_sample_data(self):
        for i in range(10):
            self.db.cursor.execute(f"""
                INSERT INTO books (title, author, publish_date, isbn)
                VALUES ('Книга{i}', 'Автор{i}', '200{i}-01-01', 'isbn-00{i}');
            """)

class BookCopies:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS book_copies (
                id SERIAL PRIMARY KEY,
                book_id INTEGER REFERENCES books(id),
                copy_number INTEGER NOT NULL,
                borrowed BOOLEAN DEFAULT FALSE
            );
        """)

    def insert_sample_data(self):
        for i in range(10):
            self.db.cursor.execute(f"""
                INSERT INTO book_copies (book_id, copy_number)
                VALUES ({i+1}, {i+10});
            """)

class BorrowRecords:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrow_records (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                book_copy_id INTEGER REFERENCES book_copies(id),
                borrow_date DATE NOT NULL,
                due_date DATE NOT NULL,
                return_date DATE,
                library_branch_id INTEGER
            );
        """)

    def insert_sample_data(self):
        for i in range(10):
            self.db.cursor.execute(f"""
                INSERT INTO borrow_records (user_id, book_copy_id, borrow_date, due_date)
                VALUES ({i+1}, {i+1}, '2023-01-0{i+1}', '2023-02-0{i+1}');
            """)

class LibraryBranches:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS library_branches (
                id SERIAL PRIMARY KEY,
                branch_name VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL
            );
        """)

    def insert_sample_data(self):
        for i in range(10):
            self.db.cursor.execute(f"""
                INSERT INTO library_branches (branch_name, location)
                VALUES ('Філія{i}', 'Місто{i}');
            """)

class Employees:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                hire_date DATE NOT NULL,
                library_branch_id INTEGER REFERENCES library_branches(id)
            );
        """)

    def insert_sample_data(self):
        for i in range(10):
            self.db.cursor.execute(f"""
                INSERT INTO employees (first_name, last_name, hire_date, library_branch_id)
                VALUES ('Працівник{i}', 'Працює{i}', '202{i}-01-01', {i+1});
            """)

# Додамо в main роботу з цими класами.

# Створили 

def main():
    random.randint(1, 10)
    HOST = "127.0.0.1"
    PORT = "5432"
    DB_NAME = "library"
    USER = "postgres"
    PASSWORD = os.environ.get('DB_PASSWORD')

    # Перевірка наявності бази
    conn_temp = psycopg2.connect(host=HOST, port=PORT, dbname="postgres", user=USER, password=PASSWORD)
    conn_temp.autocommit = True
    cursor_temp = conn_temp.cursor()
    cursor_temp.execute(f"SELECT 1 FROM pg_database WHERE lower(datname)=lower('{DB_NAME}');")
    if not cursor_temp.fetchone():
        cursor_temp.execute(f"CREATE DATABASE {DB_NAME};")
    cursor_temp.close()
    conn_temp.close()

    # Робота з базою
    db_manager = DatabaseManager(HOST, PORT, DB_NAME, USER, PASSWORD)
    
    # Створення об'єктів класів
    # book = Books(db_manager)
    # book_copies = BookCopies(db_manager)
    # borrow_records = BorrowRecords(db_manager)
    # library_branches = LibraryBranches(db_manager)
    # employees = Employees(db_manager)
    users = Users(db_manager)    

    # Список об'єктів класів
    classes_list = [users ]#, library_branches, employees, book, book_copies, borrow_records]

    # Ініціалізація та заповнення тестовими даними
    for class_obj in classes_list:
        class_obj.create_table()
        class_obj.insert_sample_data()
        

    
    # Коммітимо зміни в базу та закриваємо з'єднання
    db_manager.commit()
    db_manager.close()

if __name__ == "__main__":
    main()
