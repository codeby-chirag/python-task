from functools import wraps

import mysql.connector
import psycopg2


# Decorator
def require_database(func):
    """A decorator that ensures a database is selected before running a method."""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = self.database_check()
        current_db = result[0] if result and result[0] is not None else None

        if current_db is not None:
            print(f"Using database: {current_db}")
            return func(self, *args, **kwargs)

        else:
            print("Currently not any database used.")
            return None

    return wrapper


def enter_name(name):
    if name == "":
        print("Enter the name of Database.")
        name = input("Enter name of Database: ").strip()
        return enter_name(name)
    else:
        return name


class DatabaseOperations:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def database_check(self):
        self.cursor.execute("SELECT current_database();")
        return self.cursor.fetchone()

    def create_database(self, db_name):
        database_name = enter_name(db_name)

        self.cursor.execute(
            "SELECT datname FROM pg_database WHERE datname = %s;", (database_name,)
        )
        result = self.cursor.fetchone()

        if result is not None:
            print(f"ERROR: Database {database_name} already available.")
            return
        else:
            self.cursor.execute(f'CREATE DATABASE "{database_name}";')
            print(f"Database {database_name} created successfully.")

    def open_database(self, db_name):
        database_name = enter_name(db_name)

        self.cursor.execute(
            "SELECT * FROM pg_database WHERE datname = %s;", (database_name,)
        )
        result = self.cursor.fetchone()

        if result is None:
            print(f"ERROR: Database {database_name} not available.")
            return self.connection, self.cursor

        try:
            self.cursor.close()
            self.connection.close()

            self.connection = psycopg2.connect(
                host="127.0.0.1", user="chirag", password="c123", database=database_name
            )

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            print(f"Currently you are using '{database_name}' Database")

        except Exception as e:
            print(f"ERROR: Unable to open database '{database_name}'.")
            print(f"Error: {e}")
            return None, None

    def list_databases(self):
        self.cursor.execute("""
            SELECT datname FROM pg_database 
            WHERE datistemplate = false 
            AND datname NOT IN ('postgres', 'template0', 'template1');
        """)

        databases = self.cursor.fetchall()

        print("\nExisting Databases:")
        for db in databases:
            print(f"- {db[0]}")

    def list_tables(self):
        self.cursor.execute("SELECT current_database();")
        result = self.cursor.fetchone()

        if result is not None:
            current_db = result[0]
            print(f"Using database: {current_db}")
            print("Listing tables:")

            self.cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public';
            """)
            tables = self.cursor.fetchall()

            if tables:
                for table in tables:
                    print(f"- {table[0]}")
            else:
                print("No tables found in this database.")
        else:
            print("Currently not any database used.")

    @require_database
    def create_new_table(self, table_name, all_columns_sql):
        try:
            self.cursor.execute(f"""
                CREATE TABLE {table_name} ({all_columns_sql});
            """)
            print(f"Table '{table_name}' created successfully.")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @require_database
    def display_table_data(self, table_name):
        try:
            show_data = f"SELECT * FROM {table_name};"
            self.cursor.execute(show_data)

            column_names = [desc[0] for desc in self.cursor.description]

            records = self.cursor.fetchall()

            if records:
                print(f"\n--- Data inside table '{table_name}' ---")

                print(" | ".join(column_names))
                print("-" * (len(" | ".join(column_names)) + 4))

                for row in records:
                    print(" | ".join(str(value) for value in row))
            else:
                print(f"\nTable '{table_name}' is currently empty.")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @require_database
    def insert_record(self, table_name, all_columns, placeholder_string, val_list):

        sql = f"INSERT INTO {table_name} ({all_columns}) VALUES ({placeholder_string})"

        try:
            self.cursor.execute(sql, val_list)
            self.connection.commit()
            print("Record inserted successfully!")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @require_database
    def update_record(
        self, table_name, column_name, new_value, condition_col, uni_value
    ):

        sql = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition_col} = %s"

        try:
            self.cursor.execute(sql, (new_value, uni_value))
            self.connection.commit()
            print("Record Updated.")

            if self.cursor.rowcount == 0:
                print("No record matched your criteria. Nothing updated.")
            else:
                print("Record Updated successfully.")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @require_database
    def delete_record(self, table_name, condition_col, unique_value):

        sql = f"DELETE FROM {table_name} WHERE {condition_col} = %s"

        try:
            self.cursor.execute(sql, (unique_value,))
            self.connection.commit()

            if self.cursor.rowcount == 0:
                print("No record matched your criteria. Nothing deleted.")
            else:
                print("Record deleted successfully.")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @require_database
    def add_new_column(
        self, table_name, column_name, data_type, limit_str, constraints
    ):

        sql = f"ALTER TABLE {table_name} ADD {column_name} {data_type} {limit_str} {constraints}"

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Column added!")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @require_database
    def delete_column(self, table_name, column_name):

        sql = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Column droped!")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @require_database
    def drop_table(self, table_name):

        sql = f"DROP TABLE {table_name}"

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Table {table_name} Droped!")

        except (mysql.connector.Error, psycopg2.Error) as e:
            print("Connection failed.")
            print(f"Database Error: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def close_connection(self):
        try:
            self.cursor.close()
            self.connection.close()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


class mysqlDatabaseOperations(DatabaseOperations):
    def __init__(self, connection):
        super().__init__(connection)

    def database_check(self):
        if True:
            self.cursor.execute("SELECT DATABASE();")
            return self.cursor.fetchone()

    def create_database(self, db_name):
        database_name = enter_name(db_name)

        self.cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
        result = self.cursor.fetchone()

        if result is not None:
            print(f"ERROR: Database {database_name} already available.")
            return
        else:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            print(f"Database {database_name} created succefully.")

    def open_database(self, db_name):
        database_name = enter_name(db_name)

        self.cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
        result = self.cursor.fetchone()

        if result is not None:
            self.cursor.execute(f"USE {database_name}")
            print(f"Currently you are using '{database_name}' Database")
        else:
            print(f"ERROR: Database {database_name} not available.")
            return

    def list_databases(self):
        self.cursor.execute("SHOW DATABASES")

        databases = self.cursor.fetchall()

        print("\nExisting Databases:")
        for db in databases:
            print(f"- {db[0]}")

    def list_tables(self):
        self.cursor.execute("SELECT DATABASE();")
        current_db = self.cursor.fetchone()[0]

        if current_db is not None:
            print(f"Using database: {current_db}")
            print("Listing tables:")

            self.cursor.execute("SHOW TABLES;")
            tables = self.cursor.fetchall()

            if tables:
                for table in tables:
                    print(f"- {table[0]}")
            else:
                print("No tables found in this database.")
        else:
            print("currently not any database used")
