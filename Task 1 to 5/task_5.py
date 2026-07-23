contact_directory = {
    'John' : 123456789,
    'Tony' : 852741963
}

print("\nWhich operation you want to perform ? ")
print("\n1.Add the contact: ")
print("2.Remove the contact: ")
print("3.Update the Person details: ")
print("4.Search the contact: ")
print("5.Exit")

def add_contact():
    name = input("Enter name: ")

    if (name not in contact_directory):
        num = int(input("Enter number: "))
        contact_directory[name] = num
    else:
        print("Name already available.")

def remove_contact():
    name = input("Enter name: ")

    if (name in contact_directory):
        del contact_directory[name]
    else:
        print("Name is not available.")

def update_contact():
    detail = input("What do you want to change? Name or Number: ")

    if detail == "Name":
        name = input("Enter which name you want to change:  ")
        
        if (name in contact_directory):
            new_name = input("Enter name: ")
            contact_directory[new_name] = contact_directory.pop(name)
        else:
            print("Name is not available.")

    elif detail == "Number":
        name = input("Enter which person's contact you want to change:  ")
                
        if (name in contact_directory):
            new_num = int(input("Enter new number: "))
            contact_directory[name] = new_num
        else:
            print("Name is not available.")

def search_contact():
    detail = input("Which info you have? Name or Number: ")

    if detail == "Name":
        name = input("Enter name you want to search: ")

        if name in contact_directory:
            print(f"{name} : {contact_directory[name]}")
        else:
            print("Name not exist")

    elif detail == "Number":
        num = int(input("Enter number you want to search: "))
        
        found = False
        for name, phone in contact_directory.items():
            if phone == num:
                print(f"Name: {name}")
                found = True
                break 

        if not found:
            print("Number does not exist")

while True:
    choice = input("\n Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        remove_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        search_contact()

    elif choice == "5":
        break

    print(contact_directory)



