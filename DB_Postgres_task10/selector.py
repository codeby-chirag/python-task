from commands import (
    add_new_column,
    create_database,
    create_new_table,
    delete_column,
    delete_record,
    display_table_data,
    drop_table,
    insert_record,
    list_databases,
    list_tables,
    open_database,
    update_record,
)
from connection import get_connection

mydb = get_connection()

if mydb is not None:
    mycursor = mydb.cursor()

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
            create_database(mycursor, db_name)

        # Use database
        elif choice == "2":
            db_name = input("Enter name of Database: ").strip()
            mydb, mycursor = open_database(mydb, mycursor, db_name)
            
            if mydb is None or mycursor is None:
                print("Reconnecting to default database due to switch failure...")

            if mydb is None:
                break

        # List all databases
        elif choice == "3":
            list_databases(mycursor)

        # List all tables
        elif choice == "4":
            list_tables(mycursor)

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
        
                col_name = input("\nEnter column name (or type 'done' to finish): ").strip()
                
                if col_name.lower() == 'done':
                    if not columns:
                        print("You must add at least one column!")
                        continue
                    break
        
                print("Available types: INT, VARCHAR, TEXT, DATE")
                data_type = input(f"Enter data type for '{col_name}': ").strip().upper()
        
                limit_str = ""
                if data_type == "VARCHAR":
                    limit = input(f"Enter maximum character limit for {col_name} (e.g., 50, 200): ").strip()
                    limit_str = f"({limit})"
        
                print("Constraints (comma-separated): PRIMARY KEY, NOT NULL, UNIQUE (or press Enter for none)")
                constraints = input(f"Enter constraints for '{col_name}': ").strip().upper()
        
                column_definition = f"{col_name} {data_type}{limit_str} {constraints}".strip()
                
                columns.append(column_definition)
        
        
            all_columns_sql = ", ".join(columns)
            create_new_table(mycursor, table_name, all_columns_sql)

        # Display table data
        elif choice == "6":
            table_name = input("Enter table name: ").strip()
            display_table_data(mycursor, table_name)

        # Insert data
        elif choice == "7":
            table_name = input("Enter table name: ").strip()
            columns = []
            value = []

            while True:

                col_name = input("\nEnter column name (or type 'done' to finish): ").strip()

                if col_name.lower() == 'done':
                    break

                if not col_name:
                    print("ERROR: Column name cannot be empty.")
                    continue

                if col_name in columns:
                    print(f"Warning: Column '{col_name}' already added! Please enter a different column.")
                    continue

                col_data_type = input("Is this value in integer (Yes/No): ").strip().lower()
                col_value = input("Enter value: ").strip()

                if col_data_type == 'yes':
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
                
            insert_record(mydb, mycursor, table_name, all_columns, placeholders, value)


        # Update data
        elif choice == "8":
            table_name = input("Enter table name: ").strip()
            
            column_name = input("Enter column name: ")
            new_value = input("Enter new value: ")
            
            condition_col = input("Enter comnditional column name: ")
            unique_value = input("Enter the unique data of row: ")
            
            update_record(mydb, mycursor, table_name, column_name, new_value, condition_col, unique_value)

        # Delete data
        elif choice == "9":
            table_name = input("Enter table name: ").strip()
            
            condition_col = input("Enter comnditional column name: ")
            unique_value = input("Enter the unique data of row: ")
            
            
            delete_record(mydb, mycursor, table_name, condition_col, unique_value)

        # Add new column
        elif choice == "10":
            table_name = input("Enter table name: ").strip()
            column_name = input("Enter column name: ").strip()
            
            print("Available types: INT, VARCHAR, TEXT, DATE")
            data_type = input(f"Enter data type for '{column_name}': ").strip().upper()
            
            limit_str = ""
            if data_type == "VARCHAR":
                limit = input(f"Enter maximum character limit for '{column_name}' (e.g., 50, 200): ").strip()
                if not limit:
                    limit = "255"
                limit_str = f"({limit})"

            print("Constraints (comma-separated): PRIMARY KEY, NOT NULL, UNIQUE (Enter for none)")
            constraints = input(f"Enter constraints for '{column_name}': ").strip().upper()
                                
            add_new_column(mydb, mycursor, table_name, column_name, data_type, limit_str, constraints)
            

        # Delete column
        elif choice == "11":
            table_name = input("Enter table name: ").strip()
            column_name = input("Enter column name: ").strip()
                        
            delete_column(mydb, mycursor, table_name, column_name)

        # Drop table
        elif choice == "12":
            table_name = input("Enter table name: ").strip()

            if not table_name:
                print("ERROR: Table name cannot be empty.")
                continue

            drop_table(mydb, mycursor, table_name)

        # Exit
        elif choice == "13":
            print("Program closed.")
            mycursor.close()  
            mydb.close()      
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Authentication failed. Program stopped.")