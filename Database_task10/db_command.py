from mysql.connector import Error


def enter_name(name):
    if name == "":
        print("Enter the name of Database.")
        name = input("Enter name of Database: ").strip()
        return enter_name(name)
    else:
        return name
        
        
def create_database(mycursor, db_name):
    database_name = enter_name(db_name)
    
    mycursor.execute("SHOW DATABASES LIKE %s", (database_name,))
    result = mycursor.fetchone()
    
    if result is not None:
        print(f"ERROR: Database {database_name} already available.")
        return
    else:
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database {database_name} created succefully.")

def open_database(mycursor, db_name):
    database_name = enter_name(db_name)
    
    mycursor.execute("SHOW DATABASES LIKE %s", (database_name,))
    result = mycursor.fetchone()
    
    if result is not None:
        mycursor.execute(f"USE {database_name}")
        print(f"Currently you are using '{database_name}' Database")
    else:
        print(f"ERROR: Database {database_name} not available.")
        return
    
def list_databases(mycursor):
    mycursor.execute("SHOW DATABASES")
    
    databases = mycursor.fetchall() 
    
    print("\nExisting Databases:")
    for db in databases:
        print(f"- {db[0]}") 

def list_tables(mycursor):
    mycursor.execute("SELECT DATABASE();")
    current_db = mycursor.fetchone()[0]
    
    if current_db is not None:
        print(f"Using database: {current_db}")
        print("Listing tables:")
        
        mycursor.execute("SHOW TABLES;")
        tables = mycursor.fetchall()
        
        if tables:
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("No tables found in this database.")
    else:
        print("currently not any database used")

def create_new_table(mydb, mycursor, table_name, all_columns_sql):
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
    
    current_db = result[0] if result and result[0] is not None else None
    
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        try:
            create_table_query = f"CREATE TABLE {table_name} ({all_columns_sql});"
            mycursor.execute(create_table_query)
            print(f"Table '{table_name}' created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    else:
        print("currently not any database used")


def display_table_data(mydb, mycursor, table_name):
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
    
    current_db = result[0] if result and result[0] is not None else None
        
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        try:
            show_data = f"SELECT * FROM {table_name};"
            mycursor.execute(show_data)
            
            column_names = [desc[0] for desc in mycursor.description]
            
            records = mycursor.fetchall()

            if records:
                print(f"\n--- Data inside table '{table_name}' ---")
                
                print(" | ".join(column_names))
                print("-" * (len(" | ".join(column_names)) + 4)) 
                
                for row in records:
                    print(" | ".join(str(value) for value in row))  
            else:
                print(f"\nTable '{table_name}' is currently empty.")
                
        except Error as e:
            print(f"An error occurred: {e}")

    else:
        print("currently not any database used")


def insert_record(mydb, mycursor, table_name, all_columns, placeholder_string, val_list):
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
    
    current_db = result[0] if result and result[0] is not None else None
        
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        sql = f"INSERT INTO {table_name} ({all_columns}) VALUES ({placeholder_string})"
        
        try:
            mycursor.execute(sql, val_list)
            mydb.commit()
            print("Record inserted successfully!")
            
        except Error as e:
            print(f"Database Error: {e}")
        
    else:
        print("currently not any database used")
            

def update_record(mydb, mycursor, table_name, column_name, new_value, condition_col, uni_value):
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
    
    current_db = result[0] if result and result[0] is not None else None
        
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        sql = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition_col} = %s"
        
        try:
            mycursor.execute(sql, (new_value, uni_value))
            mydb.commit()
            print("Record Updated.")
            
            if mycursor.rowcount == 0:
                print("No record matched your criteria. Nothing updated.")
            else:
                print("Record Updated successfully.")
            
        except Error as e:
            print(f"Database Error: {e}")
        
    else:
        print("currently not any database used")
                

def delete_record(mydb, mycursor, table_name, condition_col, unique_value):
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
        
    current_db = result[0] if result and result[0] is not None else None
        
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        sql = f"DELETE FROM {table_name} WHERE {condition_col} = %s"
        
        try:
            mycursor.execute(sql, (unique_value,))
            mydb.commit()

            if mycursor.rowcount == 0:
                print("No record matched your criteria. Nothing updated.")
            else:
                print("Record Updated successfully.")
            
        except Error as e:
            print(f"Database Error: {e}")

    else:
        print("currently not any database used")
                    

def add_new_column(mydb, mycursor, table_name, column_name, data_type, limit_str, constraints):
    
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
        
    current_db = result[0] if result and result[0] is not None else None
        
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        sql = f"ALTER TABLE {table_name} ADD {column_name} {data_type} {limit_str} {constraints}"
        
        try:
            mycursor.execute(sql)
            mydb.commit()
            print("Column added!")
            
        except Error as e:
            print(f"Database Error: {e}")
        
    else:
        print("currently not any database used")
        

def delete_column(mydb, mycursor, table_name, column_name):
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
        
    current_db = result[0] if result and result[0] is not None else None
        
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        sql = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
        
        try:
            mycursor.execute(sql)
            mydb.commit()
            print("Column droped!")
            
        except Error as e:
            print(f"Database Error: {e}")
        
    else:
        print("currently not any database used")

def drop_table(mydb, mycursor, table_name):
    mycursor.execute("SELECT DATABASE();")
    result = mycursor.fetchone()
        
    current_db = result[0] if result and result[0] is not None else None
        
    if current_db is not None:
        print(f"Using database: {current_db}")
        
        sql = f"DROP TABLE {table_name}"
        
        try:
            mycursor.execute(sql)
            mydb.commit()
            print(f"Table {table_name} Droped!")
            
        except Error as e:
            print(f"Database Error: {e}")
        
    else:
        print("currently not any database used")



