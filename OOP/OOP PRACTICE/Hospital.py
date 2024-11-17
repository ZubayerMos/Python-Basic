class Hospital ():
    def __init__(self, name, Admin, Patient):
        self.name = name
        self.Admin = Admin
        self.Patient = Patient

print ("For Hospital")
hospital_name = input("Enter The Hospital name : ")
hospital_admin = input("Enter The admin name : ")
hospital_patient = input("Enter patient name :")

userHospital = Hospital(hospital_name, hospital_admin, hospital_patient)
print (f"Hospital name is {userHospital.name}\n")
print (f"Hospital admin name is {userHospital.Admin}\n")
print (f"Patient name is {userHospital.Patient}")
 
class Doctor ():
    def __init__(self, name, department, fee):
        self.name = name
        self.department = department
        self.fee = fee
       
        
print ("For Doctors")

userDoctor = input("Enter Doctor name : ")
userdepartment = input("Enter department name : ")
userfee = input("Enter Doctor fees : ")
hos_doc = Doctor(userDoctor, userdepartment, userfee)
print (f"Doctor name is {hos_doc.name}")
print (f"Doctor department is {hos_doc.department}")
print (f"Doctor fee is {hos_doc.fee}")

print ("For Doctor signin")
if userDoctor == hos_doc.name and userdepartment == hos_doc.department :
    print("Login Successful!\n")
    
    
class Patient ():
    def __init__(self, name,password, problems, phone_number):
        self.name = name
        self.password = password
        self.problems = problems
        self.phone_number = phone_number
patient_name = input("Enter patient name : ")
patient_pass = input("Enter the password : ")
patient_problem = input("Enter patient problems : ")
patient_phone = input("Enter Patient phone number : ")
user_patient = Patient(patient_name,patient_pass, patient_problem, patient_phone )

print (f"Patient name is {user_patient.name}")
print (f"Patient name is {user_patient.problems}")
print (f"Patient name is {user_patient.phone_number}")

if patient_name == user_patient.name and patient_pass == user_patient.password :
    print ("Succesfully Login!\n")
else :
    print ("Login Failed!")

    