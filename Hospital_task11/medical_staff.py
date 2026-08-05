from abc import ABC, abstractmethod


class Madicalstaff(ABC):
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
            f"Post: {self.type.title()}\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Assigned Patients: {self.assigned_patients}\n"
        )

    @staticmethod
    def display_schedule(hospital):
        while True:
            try:
                staff_id = int(input("Enter staff id: "))
                break
            except ValueError:
                print("\nError: Staff ID must be numbers. Please try again.\n")
    
        if staff_id not in hospital.medical_staff:
            print(f"Staff member with ID {staff_id} does not exist.")
            return
    
        staff_member = hospital.medical_staff[staff_id]
    
        if not staff_member.assigned_patients:
            print(f"Staff member {staff_member.name} with ID {staff_id} has no schedule (no assigned patients).")
        else:
            print(f"\n{staff_member.type.title()}: {staff_member.name}")
            print(f"Department: {staff_member.department}")
            print(f"Assigned Patients: {staff_member.assigned_patients}")
    
            if staff_member.procedures:
                print("Procedures completed:")
                for procedure in staff_member.procedures:
                    print(f" - {procedure}")
            else:
                print("Procedures: None")
        
    @abstractmethod
    def perform_procedures(self):
        pass

    @staticmethod
    def carry_out_procedure(hospital, p_id, s_id):
        if p_id not in hospital.patients:
            print(f"No patient found with ID {p_id}")
            return

        if s_id not in hospital.medical_staff:
            print(f"No staff found with ID {s_id}")
            return

        patient = hospital.patients[p_id]
        staff = hospital.medical_staff[s_id]

        if s_id not in patient.assigned_staff:
            print(f"First assign the staff member to patient {p_id}")
            return

        procedure = staff.perform_procedures()
        patient.medicalHistory.append(procedure)
        staff.procedures.append(procedure)
        print("Procedure completed successfully.")

class Doctor(Madicalstaff):
    def perform_procedures(self):
        print(f"Dr. {self.name} performed Diagnosis.")
        return "Diagnosis"


class Nurses(Madicalstaff):
    def perform_procedures(self):
        print(f"Nurse {self.name} gave Medicine.")
        return "Medicine Given"


class Surgeons(Madicalstaff):
    def perform_procedures(self):
        print(f"Surgeon {self.name} completed surgery.")
        return "Surgery"