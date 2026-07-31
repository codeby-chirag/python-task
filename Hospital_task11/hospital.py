class Hospital:
    def __init__(self):
        self.medical_staff = {}
        self.patients = {}
    
    # Register new medical staff
    def register_as_staff(self, staff_type, staff_id, name, department):

        if staff_type == "doctor":
            staff = Doctor(staff_id, staff_type, name, department)
        elif staff_type == "nurse":
            staff = Nurses(staff_id, staff_type, name, department)
        elif staff_type == "surgeon":
            staff = Surgeons(staff_id, staff_type, name, department)
        else:
            print("Invalid staff type.")
            return

        self.medical_staff[staff_id] = staff
        print("\nMedical staff registered successfully.")
                    
    # Register patients
    def register_patient(self, patient_id, patient_name, patient_age, disease, medical_history):
        
        patient = Patients(
            patient_id, patient_name, patient_age, disease, [medical_history]
        )
        self.patients[patient_id] = patient
        print("\nPatient registered successfully.")
        
    # Assign patient to medical staff
    def assign_patient_staff(self, p_id, s_id):

        if p_id not in self.patients:
            print(f"No patient found with ID {p_id}")
            return

        if s_id not in self.medical_staff:
            print(f"No staff found with ID {s_id}")
            return

        patient = self.patients[p_id]
        staff = self.medical_staff[s_id]

        staff.assigned_patients.append(patient.id)
        patient.assigned_staff.append(staff.id)

        print("Patient assigned successfully.")
    
    # Display medical staff and assigned patient
    def display_medical_staff(self):
        for staff in self.medical_staff.values():
            print(staff)
            
    # Display patients and assigned medical staff
    def display_patient(self):  
        for patient in self.patients.values():
            print(patient)

    def perform_procedures(self, p_id, s_id):

        if p_id not in self.patients:
            print(f"No patient found with ID {p_id}")
            return

        if s_id not in self.medical_staff:
            print(f"No staff found with ID {s_id}")
            return

        patient = self.patients[p_id]
        staff = self.medical_staff[s_id]

        if s_id not in patient.assigned_staff:
            print(f"First assign the staff to patient {p_id}")
            return

        procedure = staff.perform_procedures()
        patient.medicalHistory.append(procedure)
        staff.procedures.append(procedure)

        print("Procedure completed successfully.")
        
    # Update patient detail
    def update_patient_data(self, patient_id, field, value):

        if patient_id not in self.patients:
            print("Patient not found.")
            return

        patient = self.patients[patient_id]

        if field == "name":
            patient.name = value

        elif field == "age":
            patient.age = value

        elif field == "disease":
            patient.dicsease = value

        elif field == "history":
            patient.medicalHistory.append(value)

        print("Patient record updated successfully.")
        
    def display_staff_schedule(self):
        for staff in self.medical_staff.values():
            staff.display_schedule()
        
class Madicalstaff:
    # Name #Id #Department #Assign patient
    def __init__(self, id, type, name, department):
        self.id = id
        self.type = type
        self.name = name
        self.department = department
        self.assigned_patients = []
        self.procedures = []
        
    def __str__(self):
        return (
        f"ID: {self.id}\n"
        f"Post: {self.type}\n"
        f"Name: {self.name}\n"
        f"Department: {self.department}\n"
        f"Assigned Patients: {self.assigned_patients}\n"
    )

    def perform_procedures(self):
        pass
    
    def display_schedule(self):
        print(f"{self.type.title()}: {self.name}\n")
        print(f"Department: {self.department}\n")
        print(f"Assigned Patients: {self.assigned_patients}\n")

        if self.procedures:
            print("Procedures:")
            for procedure in self.procedures:
                print(f" - {procedure}")
        else:
            print("Procedures: None")

class Doctor(Madicalstaff):
    def perform_procedures(self):
        print(f"Dr. {self.name} performed Diagnosis.")
        return "Diagnosis"
    
    # doctore.display_schedule()
    
class Nurses(Madicalstaff): 
    def perform_procedures(self):
        print(f"Nurse {self.name} gave Medicine.")
        return "Medicine Given"
    
    # nurses.display_schedule()

    
class Surgeons(Madicalstaff):
    def perform_procedures(self):
        print(f"Surgeon {self.name} completed surgery.")
        return "Surgery"
        
    # surgeons.display_schedule()

class Patients:
    # Id  # Name  # Age  # Dicsease  # Medical history  # Assign staff
    def __init__(self, id, name, age, dicsease, medicalHistory):
        self.id = id
        self.name = name
        self.age = age
        self.dicsease = dicsease
        self.medicalHistory = medicalHistory
        self.assigned_staff = []
            
    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Dicsease: {self.dicsease}\n"
            f"Medical History: {self.medicalHistory}\n"
            f"Assigned Staff: {self.assigned_staff}\n"
    )
    
    # Update patient data
    # def update_patient_data():
    #     patient.medicalHistory.append("Blood Test")
    
hospital = Hospital()

while True:
    print("\n1. Register as new Medical staff.")
    print("2. Register as Patient.")
    print("3. Assign patients to medical staff members.")
    print("4. Display all registered medical staff members and their assigned patients.")
    print("5. Display all registered patients and their assigned medical staff members.")
    print("6. Perform medical procedures.")
    print("7. Update patient records.")
    print("8. Display the schedule of each medical staff.")
    print("9. Exit")
    
    
    choice = input("\nEnter choice: ")
    
    if choice == "1":
        staff_type = input("Enter staff type (doctor/nurse/surgeon): ").lower()
        staff_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        
        hospital.register_as_staff(staff_type, staff_id, name, department)
    
    elif choice == "2":  
        patient_id = int(input("Enter Patient ID: "))
        patient_name = input("Enter Name: ")
        patient_age = input("Enter Age: ")
        disease = input("Enter Disease: ")
        medical_history = input("Enter Medical History: ")
        
        hospital.register_patient(patient_id, patient_name, patient_age, disease, medical_history)
        
    elif choice == "3":
        patient_id = int(input("Enter Patient ID: "))
        staff_id = int(input("Enter staff id: "))
        
        hospital.assign_patient_staff(patient_id, staff_id)
        
    elif choice == "4":
        hospital.display_medical_staff()
    
    elif choice == "5":
        hospital.display_patient()
        
    elif choice == "6":
        p_id = int(input("Enter patient id: "))
        s_id = int(input("Enter staff id: "))
        
        hospital.perform_procedures(p_id, s_id)
    
    elif choice == "7":
        patient_id = int(input("Enter patient ID: "))
        
        hospital.display_patient()
        
        update_value = input(f"which info of {patient_id} you want to Update: ")
        
        if update_value.lower() == "name":
            up_name = input("Enter new name: ")
            hospital.update_patient_data(patient_id, "name", up_name)
            
        elif update_value.lower() == "age":
            up_age = input("Enter new age: ")
            hospital.update_patient_data(patient_id, "age", up_age)
            
        elif update_value.lower() == "disease":
            up_disease = input("Enter new Disease: ")
            hospital.update_patient_data(patient_id, "disease", up_disease)

        elif update_value.lower() == "history":
            up_history = input("Enter history: ")
            hospital.update_patient_data(patient_id, "history", up_history)

        else:
            print("Invalide input.")
            
    elif choice == "8":
        hospital.display_staff_schedule()
    
    elif choice == "9":
        break
        
    else:
        print("Invalid choice. Please try again.")