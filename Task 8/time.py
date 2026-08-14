import re
from datetime import timedelta


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    
    def calculate(self, total_sec):
        h = (total_sec // 3600) % 24
        m = (total_sec % 3600) // 60
        s = total_sec % 60
        return type(self)(h, m, s)
        
    def __add__(self, other):
        result_duration = self.duration + other.duration
        total_sec = int(result_duration.total_seconds())
        return self.calculate(total_sec)
    
    def __sub__(self, other):
        result_duration = self.duration - other.duration
        total_sec = int(result_duration.total_seconds())
        return self.calculate(total_sec)
    
    def increment(self):
        update_part = input("Enter what you want to increment (hrs, mit, sec): ").strip().lower()
        amount = int(input("Enter value to add: "))
        
        current_total_sec = int(self.duration.total_seconds())
        
        if update_part == "hrs":
            current_total_sec += amount * 3600
        elif update_part == "mit":
            current_total_sec += amount * 60
        elif update_part == "sec":
            current_total_sec += amount
        else:
            print("Invalid option! No increment applied.")
            return self
            
        return self.calculate(current_total_sec)
        
    def __str__(self):
        total_sec = int(self.duration.total_seconds())
        h = (total_sec // 3600) % 24
        m = (total_sec % 3600) // 60
        s = total_sec % 60
        return f"{h:02d}:{m:02d}:{s:02d}"


def validate_inp_time(inp_time):
    pattern = r"^\d{2}:\d{2}:\d{2}$"
    
    if re.match(pattern, inp_time):
        return inp_time
    print("Enter time with valid format.")
    Y = input("Enter time with format HH:MM:SS: ")
    return validate_inp_time(Y)


def input_time(choice):
    if choice == "1":
        user_input = input("Enter base time (HH:MM:SS): ")
        validated = validate_inp_time(user_input)
        h, m, s = validated.split(':')
        t = Time(int(h), int(m), int(s))
        
        return t
        
    elif choice == "2" or choice == "3":
        user_input_t1 = input("Enter time 1 (HH:MM:SS): ")
        x1 = validate_inp_time(user_input_t1)
        h, m, s = x1.split(':')
        time1 = Time(int(h), int(m), int(s))
            
        user_input_t2 = input("Enter time 2 (HH:MM:SS): ")
        x2 = validate_inp_time(user_input_t2)
        x, y, z = x2.split(':')
        time2 = Time(int(x), int(y), int(z))
        
        return time1, time2


while True:
    print("\n1. Increase Time")
    print("2. Add Time")
    print("3. Subtract Time")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        t = input_time(choice)
        updated_time = t.increment()
        print("Updated Time:", updated_time)
    
    elif choice == "2":  
        t1, t2 = input_time(choice)
        new_additional_time = t1 + t2
        print("Result:", new_additional_time)
        
    elif choice == "3":
        t1, t2 = input_time(choice)
        new_substraction_time = t1 - t2
        print("Result:", new_substraction_time)
        
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
