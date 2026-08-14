import psycopg2

def get_connection():
    correct_username = "user1"
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
        mydb = psycopg2.connect(
            host = "127.0.0.1",
            user = correct_username,
            password = correct_password,
            database = "postgres" 
        )
        
        
        mydb.autocommit = True

        print("Login successful.")
        print("Connected to PostgreSQL server.")
        return mydb

    except Exception as e:  
        print("Connection failed.")
        print(f"Error: {e}")
        return None
