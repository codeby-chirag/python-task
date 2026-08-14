from hospital import Hospital
from medical_staff import Doctor, Madicalstaff, Nurses, Surgeons
from patient import Patients

hospital = Hospital()

while True:
    print("""\nChoice the operation you want to perform:
        1. Register as new Medical staff.
        2. Register as Patient.
        3. Assign patients to medical staff members.
        4. Display all registered medical staff members.
        5. Display all registered patients.
        6. Perform medical procedures.
        7. Update patient records.
        8. Display the schedule of each medical staff.
        9. Exit"""
    )

    choice = input("\nEnter choice: ")

    if choice == "1":
        while True:
            try:
                staff_type = input("Enter staff type (doctor/nurse/surgeon): ").lower()
                staff_id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                department = input("Enter Department: ")
                break
            except ValueError:
                print("\nError: Staff ID must be numbers. Please try again.\n")

        if staff_type == "doctor":
            staff = Doctor(staff_id, staff_type, name, department)
        elif staff_type == "nurse":
            staff = Nurses(staff_id, staff_type, name, department)
        elif staff_type == "surgeon":
            staff = Surgeons(staff_id, staff_type, name, department)
        else:
            print("Invalid staff type.")
            staff = None

        if staff:
            hospital.register_staff(staff) 
    
    elif choice == "2":
        while True:
            try:
                patient_id = int(input("Enter Patient ID: "))
                patient_name = input("Enter Name: ")
                patient_age = int(input("Enter Age: "))
                disease = input("Enter Disease: ")
                medical_history = input("Enter Medical History: ")
                break
            except ValueError:
                print("\nError: Patient ID and Age must be integers. Please try again.\n")

        new_patient = Patients(patient_id, patient_name, patient_age, disease, [medical_history])

        hospital.register_patient(new_patient)

    elif choice == "3":
        try:
            p_id = int(input("Enter Patient ID: "))
            s_id = int(input("Enter Staff ID: "))
            hospital.assign_patient_staff(p_id, s_id)
        except ValueError:
            print("IDs must be integers.")

    elif choice == "4":
        print("\n--- Medical Staff Directory ---")
        hospital.display_medical_staff()

    elif choice == "5":
        print("\n--- Patient Directory ---")
        hospital.display_patient()

    elif choice == "6":
        try:
            p_id = int(input("Enter Patient ID: "))
            s_id = int(input("Enter Staff ID: "))
            Madicalstaff.carry_out_procedure(hospital, p_id, s_id)
        except ValueError:
            print("IDs must be integers.")

    elif choice == "7":
        try:
            patient_id = int(input("Enter Patient ID: "))
            print("Fields to update: name, age, disease, history")
            field = input("Enter field name: ").lower()
            value = input("Enter new value: ")
            if field == "age":
                value = int(value)
            Patients.update_patient_data(hospital, patient_id, field, value)
        except ValueError:
            print("Age must be an integer.")

    elif choice == "8":
        Madicalstaff.display_schedule(hospital)

    elif choice == "9":
        print("Exiting hospital system.")
        break
    else:
        print("Invalid choice. Choose 1-9.")