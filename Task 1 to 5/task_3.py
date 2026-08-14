print("Enter use name with this conditions: ")
print("     ○ username should have atleast one '.' ")
print("     ○ username should have atleast one '_' ")
print("     ○ username should have atleast be 8 in length ")

while True:
    user_name = input("Enter user name: ")

    if ('.' not in user_name or '_' not in user_name or len(user_name) < 8):
        print(" Error: Your user name doesnt have '.' and '_'. And make sure it containe 8 ot more characters.")
    else:
        print(user_name)
        break


print("Enter Password with this conditions: ")
print("     ○ Atleast one of the following '@,#,$,%' ")
print("     ○ Atleast one Uppercase letter ")
print("     ○ Atleast one Lowercase letter ")
print("     ○ Atleast one digit 0-9 ")

items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:

    user_password = input("Enter the Password: ")

    if not any(char in user_password for char in ['@', '#', '$', '%']):
        print("Error: Your password doesn't have @, #, $ or %")

    elif (not any(char2.islower() for char2 in user_password)):
        print("Error: Password must have 1 LowerCase")

    elif (not any(char1.isupper() for char1 in user_password)):
        print("Error: Password must have 1 UpperCase")

    elif not any(i in user_password for i in items):
        print("Error: Password must have digit from 0-9 ")

    else:
        print(user_password)
        break




