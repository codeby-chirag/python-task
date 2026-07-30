hospital = {
    "medical_staff": {
        "doctors": {
            1001: {
                "name": "John",
                "department": "Physio",
                "assigned_patients": [2001, 2002]
            },
            1002: {
                "name": "David",
                "department": "Cardiology",
                "assigned_patients": []
            }
        },

        "nurses": {
            1101: {
                "name": "Lina",
                "department": "Physio",
                "assigned_patients": [2001]
            }
        },

        "surgeons": {
            1201: {
                "name": "Sam",
                "department": "Orthopedic",
                "assigned_patients": [2003]
            }
        }
    },

    "patients": {
        2001: {
            "name": "Roman",
            "age": 35,
            "disease": "Fracture",
            "medical_history": ["X-Ray", "Pain Killer"],
            "assigned_staff": [1001, 1101]
        },

        2002: {
            "name": "Rahul",
            "age": 42,
            "disease": "Back Pain",
            "medical_history": [],
            "assigned_staff": [1001]
        },

        2003: {
            "name": "Amit",
            "age": 50,
            "disease": "Knee Injury",
            "medical_history": ["MRI"],
            "assigned_staff": [1201]
        }
    }
}

class Hospital:
    def __init__(self):
        self.medical_staff = []
        self.patients = []
        
    # Register new medical staff
    def register_as_staff(self):
        staff_type = input("Enter staff type (doctor/nurse/surgeon): ").lower()
        staff_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")

        if staff_type == "doctor":
            staff = Doctor(staff_id, name, department)
        elif staff_type == "nurse":
            staff = Nurses(staff_id, name, department)
        elif staff_type == "surgeon":
            staff = Surgeons(staff_id, name, department)
        else:
            print("Invalid staff type.")
            return

        self.medical_staff.append(staff)
        print("Medical staff registered successfully.")
        
    # Register patients
    def register_patient(self):
            pass
        
    # Assign patient to medical staff
    
    # Display medical staff and assigned patient
    def display_medical_staff(self):
        pass
    # Display patients and assigned medical staff
    def display_patient(self):  
            pass

class Madicalstaff:
    # Name #Id #Department #Assign patient
    def __init__(self, id, name, department, assignPatients=0):
        self.id = id
        self.name = name
        self.department = department
        self.assignPatients = assignPatients
        
    def perform_procedures():
        # Perform procedures
        pass
    
    def display_schedule():
        # Display Schedule of Doctor, Nurses, Surgeons
        pass

class Doctor(Madicalstaff):
    def perform_procedures():
        # Perform procedure : Diagonsis
        pass
    
    # doctore.display_schedule()
    
class Nurses(Madicalstaff): 
    def perform_procedures():
        # Perform procedure : Giving Medicine
        pass
    
    # nurses.display_schedule()

    
class Surgeons(Madicalstaff):
    def perform_procedures():
        # Perform procedure : Surgery
        pass
    
    # surgeons.display_schedule()

class Patients:
    # Id  # Name  # Age  # Dicsease  # Medical history  # Assign staff
    def __init__(self, id, name, age, dicsease, medicalHistory, assignStaff):
            self.id = id
            self.name = name
            self.age = age
            self.dicsease = dicsease
            self.medicalHistory = medicalHistory
            self.assignStaff = assignStaff
    
    # Update patient data
    def update_patient_data():
        pass
    

while True:
    print("\n1. Register as new Medical staff.")
    print("2. Register as Patient.")
    print("3. Assign patients to medical staff members.")
    print("4. Display all registered medical staff members and their assigned patients.")
    print("5. Display all registered patients and their assigned medical staff members.")
    print("6. Perform medical procedures.")
    print("7. Update patient records.")
    print("8. Display the schedule of each medical staff.")
    
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        x = Hospital()
        x.register_as_staff()
    
    elif choice == "2":  # noqa: SIM114
        pass
        
    elif choice == "3":
        pass
        
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")