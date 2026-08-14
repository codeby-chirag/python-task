class Hospital:
    def __init__(self):
        self.medical_staff = {}
        self.patients = {}

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

        if patient.id in staff.assigned_patients:
            print(f"Staff member {staff.name} is already assigned to patient {patient.name}.")
            return

        staff.assigned_patients.append(f"{patient.id} : {patient.name}")
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
    
    def register_staff(self, staff):
        if staff.id in self.medical_staff:
            print(f"Error: Staff ID {staff.id} is already registered.")
            return
        
        self.medical_staff[staff.id] = staff
        print("\nMedical staff registered successfully.")
        
    def register_patient(self, patient):
        if patient.id in self.patients:
            print(f"Error: Patient ID {patient.id} is already registered to {self.patients[patient.id].name}.")
            return

        self.patients[patient.id] = patient
        print("\nPatient registered successfully.")