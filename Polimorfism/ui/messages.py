def general_presentation():
    print("Welcome!!")
    print("Next you can find the hospital and doctor details \n")


def insert_hospital_name():
    print("Insert the hospital name, please: ")
    return input()


def insert_doctor_id():
    print("Insert the doctor id, please: ")
    return input()

def show_information_hospital(records):
    print("-------------------------------------")
    print("\tHospital Record")
    print("-------------------------------------")
    for row in records:
        print("Hospital Id:", row[0], )
        print("Hospital Name:", row[1])
        print("Bed Count:", row[2])

def show_information_doctor(records):
    print("-------------------------------------")
    print("\tDoctor Record")
    print("-------------------------------------")
    for row in records:
        print("Doctor Id:", row[0])
        print("Doctor Name:", row[1])
        print("Hospital Id:", row[2])
        print("Joining Date:", row[3])
        print("Specialty:", row[4])
        print("Salary:", row[5])
        print("Experience:", row[6])
