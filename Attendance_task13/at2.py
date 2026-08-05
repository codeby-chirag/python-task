import random


class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.attendance_records = [] 
        
    def add_student(self, student_name, student_id, student_class, student_rollno):
        new_student = Student(student_name, student_id, student_class, student_rollno)
        self.students[student_id] = new_student
        print(f"Successfully added Student: {student_name} with ID: {student_id}")

    def add_teacher(self, teacher_name, teacher_id, teacher_subject_taught):
        new_teacher = Teacher(teacher_name, teacher_id, teacher_subject_taught)
        self.teachers[teacher_id] = new_teacher
        print(f"Successfully added Teacher: {teacher_name} with ID: {teacher_id}")

    def get_verified_id(self, user_type):
        input_id = int(input(f"Enter {user_type} id: "))
        
        if user_type == "Teacher":
            if input_id in self.teachers:
                teacher_object = self.teachers[input_id]
                return teacher_object.get_id()
            else:
                print("Enter valid Teacher id!")
                return self.get_verified_id("Teacher")  
                
        elif user_type == "Student":
            if input_id in self.students:
                student_object = self.students[input_id]
                return student_object.get_id()
            else:
                print("Enter valid Student id!")
                return self.get_verified_id("Student") 

    def mark_attendance(self, student_id, date, status):
        new_record = Attendance(student_id, date, status)
        self.attendance_records.append(new_record)
        
        student_name = self.students[student_id].get_name()
        print(f"Attendance '{status}' successfully marked for {student_name} on {date}.")


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
        

# Main execution environment
my_school = SchoolManagementSystem()
        
while True:
    print("""\nChoice Operation:
        1. Add Student
        2. Add Teacher
        3. Mark attendance for student.
        4. Generate attendance report for perticuler date range.
        5. Exit 
    """)
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        student_name = input("Enter name of student: ")
        
        student_id = 220 + random.randint(0, 9999)
        while student_id in my_school.students or student_id in my_school.teachers:
            student_id = 220 + random.randint(0, 9999)
        
        student_class = input("Enter class of student: ")
        student_rollno = int(input("Enter student roll number: "))
        
        my_school.add_student(student_name, student_id, student_class, student_rollno)
        
    elif choice == "2":
        teacher_name = input("Enter name of teacher: ")
        
        teacher_id = 220 + random.randint(0, 9999)
        while teacher_id in my_school.students or teacher_id in my_school.teachers:
            teacher_id = 220 + random.randint(0, 9999)
        
        teacher_subject_taught = input("Enter subject of teacher: ")        
        my_school.add_teacher(teacher_name, teacher_id, teacher_subject_taught)
        
    elif choice == "3":
        # System handles the lookup internally via its own method
        verified_teacher_id = my_school.get_verified_id("Teacher")
        print("Teacher id verified!")

        verified_student_id = my_school.get_verified_id("Student")
        print("Student id verified!")
        
        # Collect attendance details now that both IDs are 100% verified
        date = input("Enter date (DD-MM-YYYY): ")
        status = input("Enter status (Present/Absent): ").strip().title()
        
        # Call the management system to record it
        my_school.mark_attendance(verified_student_id, date, status)

    elif choice == "5":
        break
