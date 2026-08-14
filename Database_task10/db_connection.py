import mysql.connector
from mysql.connector import Error


def get_connection():
    correct_username = "user1"
    correct_password = "chirag123"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username:
        print("Invalid username.")
        return None

    if password != correct_password:
        print("Invalid password.")
        return None

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=correct_username,
            password=correct_password
        )

        if mydb.is_connected():
            print("Login successful.")
            print("Connected to MySQL server.")

            return mydb

    except mydb.connector.Error as e:
        print("Connection failed.")
        print(f"Error: {e}")

    return None