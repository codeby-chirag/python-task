class Patients:
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
            f"Disease: {self.dicsease}\n"
            f"Medical History: {self.medicalHistory}\n"
            f"Assigned Staff: {self.assigned_staff}\n"
        )
        
    @staticmethod
    def update_patient_data(hospital, patient_id, field, value):
        if patient_id not in hospital.patients:
            print("Patient not found.")
            return

        patient = hospital.patients[patient_id]

        if field == "name":
            patient.name = value
        elif field == "age":
            patient.age = value
        elif field == "disease":
            patient.dicsease = value
        elif field == "history":
            patient.medicalHistory.append(value)

        print("Patient record updated successfully.")