from commands import DatabaseOperations, mysqlDatabaseOperations
from connection import get_connection


def main():

    print("=== Database Selector ===")
    print("1. MySQL")
    print("2. PostgreSQL")

    db_choice = input("Choose your database (1 or 2): ")

    conn = get_connection(db_choice)

    if not conn:
        print("Exiting due to connection failure.")
        return

    if db_choice == "1":
        db_ops = mysqlDatabaseOperations(conn)
    elif db_choice == "2":
        db_ops = DatabaseOperations(conn)
    else:
        print("Invalid choice!")

    while True:
        print("""
    Choose the operation.

    1. Create Database
    2. Open Existing Database
    3. List All Existing Databases
    4. List All Tables
    5. Create New Table
    6. Display Data of Table
    7. Insert Records
    8. Update Records
    9. Delete Records
    10. Add New Column
    11. Delete Existing Column
    12. Drop Table
    13. Exit
        """)

        choice = input("Enter your choice: ")

        # Create database
        if choice == "1":
            db_name = input("Enter name of Database: ").strip()
            db_ops.create_database(db_name)

        # Use database
        elif choice == "2":
            db_name = input("Enter name of Database: ").strip()
            db_ops.open_database(db_name)

        # List all databases
        elif choice == "3":
            db_ops.list_databases()

        # List all tables
        elif choice == "4":
            db_ops.list_tables()

        # Create new table
        elif choice == "5":
            table_name = input("Enter table name: ").strip()

            if not table_name:
                print("ERROR: Table name cannot be empty.")
                continue

            columns = []
            adding_columns = True

            print("\n--- Define your columns ---")
            while adding_columns:

                col_name = input(
                    "\nEnter column name (or type 'done' to finish): "
                ).strip()

                if col_name.lower() == "done":
                    if not columns:
                        print("You must add at least one column!")
                        continue
                    break

                print("Available types: INT, VARCHAR, TEXT, DATE")
                data_type = input(f"Enter data type for '{col_name}': ").strip().upper()

                limit_str = ""
                if data_type == "VARCHAR":
                    limit = input(
                        f"Enter maximum character limit for {col_name} (e.g., 50, 200): "
                    ).strip()
                    limit_str = f"({limit})"

                print(
                    "Constraints (comma-separated): PRIMARY KEY, NOT NULL, UNIQUE (or press Enter for none)"
                )
                constraints = (
                    input(f"Enter constraints for '{col_name}': ").strip().upper()
                )

                column_definition = (
                    f"{col_name} {data_type}{limit_str} {constraints}".strip()
                )

                columns.append(column_definition)

            all_columns_sql = ", ".join(columns)
            db_ops.create_new_table(table_name, all_columns_sql)

        # Display table data
        elif choice == "6":
            table_name = input("Enter table name: ").strip()
            db_ops.display_table_data(table_name)

        # Insert data
        elif choice == "7":
            table_name = input("Enter table name: ").strip()
            columns = []
            value = []

            while True:

                col_name = input(
                    "\nEnter column name (or type 'done' to finish): "
                ).strip()

                if col_name.lower() == "done":
                    break

                if not col_name:
                    print("ERROR: Column name cannot be empty.")
                    continue

                if col_name in columns:
                    print(
                        f"Warning: Column '{col_name}' already added! Please enter a different column."
                    )
                    continue

                col_data_type = (
                    input("Is this value in integer (Yes/No): ").strip().lower()
                )
                col_value = input("Enter value: ").strip()

                if col_data_type == "yes":
                    try:
                        col_value = int(col_value)
                    except ValueError:
                        print("ERROR: Enter valid integer.")
                        continue

                columns.append(col_name)
                value.append(col_value)

            if not columns:
                print("No data entered.")
                continue

            all_columns = ", ".join(columns)

            placeholders = ", ".join(["%s"] * len(columns))

            db_ops.insert_record(table_name, all_columns, placeholders, value)

        # Update data
        elif choice == "8":
            table_name = input("Enter table name: ").strip()

            column_name = input("Enter column name: ")
            new_value = input("Enter new value: ")

            condition_col = input("Enter comnditional column name: ")
            unique_value = input("Enter the unique data of row: ")

            db_ops.update_record(
                table_name, column_name, new_value, condition_col, unique_value
            )

        # Delete data
        elif choice == "9":
            table_name = input("Enter table name: ").strip()

            condition_col = input("Enter comnditional column name: ")
            unique_value = input("Enter the unique data of row: ")

            db_ops.delete_record(table_name, condition_col, unique_value)

        # Add new column
        elif choice == "10":
            table_name = input("Enter table name: ").strip()
            column_name = input("Enter column name: ").strip()

            print("Available types: INT, VARCHAR, TEXT, DATE")
            data_type = input(f"Enter data type for '{column_name}': ").strip().upper()

            limit_str = ""
            if data_type == "VARCHAR":
                limit = input(
                    f"Enter maximum character limit for '{column_name}' (e.g., 50, 200): "
                ).strip()
                if not limit:
                    limit = "255"
                limit_str = f"({limit})"

            print(
                "Constraints (comma-separated): PRIMARY KEY, NOT NULL, UNIQUE (Enter for none)"
            )
            constraints = (
                input(f"Enter constraints for '{column_name}': ").strip().upper()
            )

            db_ops.add_new_column(
                table_name, column_name, data_type, limit_str, constraints
            )

        # Delete column
        elif choice == "11":
            table_name = input("Enter table name: ").strip()
            column_name = input("Enter column name: ").strip()

            db_ops.delete_column(table_name, column_name)

        # Drop table
        elif choice == "12":
            table_name = input("Enter table name: ").strip()

            if not table_name:
                print("ERROR: Table name cannot be empty.")
                continue

            db_ops.drop_table(table_name)

        # Exit
        elif choice == "13":
            print("Program closed.")
            db_ops.close_connection()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
