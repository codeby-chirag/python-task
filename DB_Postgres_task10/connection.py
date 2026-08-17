import mysql.connector
import psycopg2


def get_connection(db_choice):
    """Returns a database connection based on user input."""

    correct_username = "chirag"
    correct_password = "c123"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username:
        print("Invalid username.")
        return None

    if password != correct_password:
        print("Invalid password.")
        return None

    try:
        if db_choice == "1":
            print("Connecting to MySQL...")
            mydb = mysql.connector.connect(
                host="localhost", user=correct_username, password=correct_password
            )

            if mydb.is_connected():
                print("Login successful.")
                print("Connected to MySQL server.")

                return mydb

        elif db_choice == "2":
            print("Connecting to PostgreSQL...")

            mydb = psycopg2.connect(
                host="127.0.0.1",
                user=correct_username,
                password=correct_password,
                database="postgres",
            )

            mydb.autocommit = True

            print("Login successful.")
            print("Connected to PostgreSQL server.")
            return mydb

        else:
            print("Invalid choice.")
            return None

    except (mysql.connector.Error, psycopg2.Error) as e:
        print("Connection failed.")
        print(f"Database Error: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None