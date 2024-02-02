import sqlite3
from sqlite3 import Error

# Function to create a connection to the SQLite database
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('registration.db')
        print("Connection to SQLite DB successful")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to create the 'Registration' table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Registration (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR(255) NOT NULL,
                Email VARCHAR(255) NOT NULL,
                DateOfBirth DATE,
                CONSTRAINT unique_email UNIQUE (Email)
            )
        ''')
        connection.commit()
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to insert a new record
def create_record(connection, name, email, dob):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Registration (Name, Email, DateOfBirth)
            VALUES (?, ?, ?)
        ''', (name, email, dob))
        connection.commit()
        print("Record created successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to retrieve records
def read_records(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Registration")
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")

# Function to update a record
def update_record(connection, record_id, new_email):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE Registration
            SET Email = ?
            WHERE ID = ?
        ''', (new_email, record_id))
        connection.commit()
        print("Record updated successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to delete a record
def delete_record(connection, record_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Registration WHERE ID = ?", (record_id,))
        connection.commit()
        print("Record deleted successfully")
    except Error as e:
        print(f"Error: {e}")

# Main function
def main():
    connection = create_connection()
    if connection:
        create_table(connection)

        create_record(connection, "John Doe", "john.doe@example.com", "1990-01-01")
        create_record(connection, "Jane Smith", "jane.smith@example.com", "1985-05-15")

        read_records(connection)

        update_record(connection, 1, "john.doe.updated@example.com")

        read_records(connection)

        delete_record(connection, 2)

        read_records(connection)

        connection.close()

if __name__ == "__main__":
    main()
