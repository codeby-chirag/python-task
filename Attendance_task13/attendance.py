import random


class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.attendance_records = {} 

    def add_student(self, student_name, student_id, student_class, student_rollno):
        
        new_student = Student(student_name, student_id, student_class, student_rollno)
        self.students[student_id] = new_student
        
        print(f"Successfully added Student: {student_name} with ID: {student_id}")

    def add_teacher(self, teacher_name, teacher_id, teacher_subject_taught):
        
        new_teacher = Teacher(teacher_name, teacher_id, teacher_subject_taught)
        self.teachers[teacher_id] = new_teacher
        
        print(f"Successfully added Teacher: {teacher_name} with ID: {teacher_id}")
        print(f"Assigned to teach: {new_teacher.get_subject()}")

    def get_verified_id(self, user_type):
        while True:
            try:
                input_id = int(input(f"\nEnter {user_type} id: "))
            except ValueError:
                print("Invalid input format. Please enter numbers only.")
                continue

            if user_type == "Teacher":
                if input_id in self.teachers:
                    return input_id
                print("Enter valid Teacher id!")
            elif user_type == "Student":
                if input_id in self.students:
                    return input_id
                print("Enter valid Student id!")

    def mark_attendance(self, s_id, date, status):
        
        student_record = Attendance(s_id, date, status)
        
        if s_id not in self.attendance_records:
            self.attendance_records[s_id] = []
            
        self.attendance_records[s_id].append(student_record)
        print(f"Successfully attendance marked of student {s_id} for date {date}")

    def generate_report(self, s_id):
        if s_id not in self.students:
            print("Enter valid student id.")
            return
            
        student = self.students[s_id]
        print(f"\n--- Attendance Report for {student.get_name()} ---")
        print(f"Class: {student.get_class()}")        
        print(f"Roll Number: {student.get_roll_number()}")
        
        records = self.attendance_records.get(s_id, [])
        if not records:
            print("No history found for this student.")
            return
            
        for record in records:
            print(f"Date: {record.date} | Status: {record.status}")

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def get_name(self):
        return self.name
        
    def get_id(self):
        return self.id

class Student(Person):
    def __init__(self, name, id, s_class, roll_number):
        super().__init__(name, id) 
        self.s_class = s_class
        self.roll_number = roll_number
        
    def get_class(self):
        return self.s_class
    
    def get_roll_number(self):
        return self.roll_number

class Teacher(Person):
    def __init__(self, name, id, subject_taught):
        super().__init__(name, id)
        self.subject_taught = subject_taught
        
    def get_subject(self):
        return self.subject_taught
    
class Attendance:
    def __init__(self, student_id, date, status):
        self.student_id = student_id
        self.date = date
        self.status = status

my_school = SchoolManagementSystem()

while True:
    print("""\nChoice Operation:
    1. Add Student
    2. Add Teacher
    3. Mark attendance for student.
    4. Generate attendance report for student.
    5. Exit
    """)
    
    choice = input("Enter you choice: ").strip()
    
    if choice == "1":
        student_name = input("Enter name of student: ")
        
        student_id = 220 + random.randint(0, 9999)
        while student_id in my_school.students:
            student_id = 220 + random.randint(0, 9999)
            
        student_class = input("Enter class of student: ")
        
        try:
            student_rollno = int(input("Enter student roll number: "))
        except ValueError:
            print("Invalid roll number format. Defaulting to 0.")
            student_rollno = 0
        my_school.add_student(student_name, student_id, student_class, student_rollno)
        
    elif choice == "2":
        teacher_name = input("Enter name of teacher: ")
        teacher_id = 220 + random.randint(0, 9999)

        while teacher_id in my_school.teachers:
            teacher_id = 220 + random.randint(0, 9999)
            
        teacher_subject_taught = input("Enter subject of teacher: ")       
        my_school.add_teacher(teacher_name, teacher_id, teacher_subject_taught)
        
    elif choice == "3":
        
        verified_teacher_id = my_school.get_verified_id("Teacher")
        teacher_obj = my_school.teachers[verified_teacher_id]
        print(f"\nTeacher Verified: {teacher_obj.get_name()}")
        print(f"Subject Taught: {teacher_obj.get_subject()}") 
                
        verified_student_id = my_school.get_verified_id("Student")
        print("\nStudent id verified!")
        
        date = input("\nEnter date (DD-MM-YYYY): ")
        status = input("Enter status (Present/Absent): ").strip().title()
        
        my_school.mark_attendance(verified_student_id, date, status)
        
    elif choice == "4":
        student_id = my_school.get_verified_id("Student")
        my_school.generate_report(student_id)
        
    elif choice == "5":
        print("Exiting system.")
        break
    else:
        print("Invalid operation selection.")
