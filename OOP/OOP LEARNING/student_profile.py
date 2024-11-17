import datetime
current_datetime = datetime.datetime.now()

class Studentprofile():
    def __init__(self, name, id, department, university):
        self.name = name
        self.id = id
        self.department = department
        self.university = university
    def student_profile(self):
        print (f"Student name is {self.name} \n Student id is {self.id} \n Student department is {self.department} Student university is {self.university}")
print ("For Student 1")
username = input("Enter Student Name : ")
userid = input("Enter Student Id : ")
userdep = input("Enter Student Department : ")
useruni = input("Enter Student University Name : ")

print ("For Student 2")

username2= input("Enter Student Name : ")
userid2 = input("Enter Student Id : ")
userdep2 = input("Enter Student Department : ")
useruni2 = input("Enter Student University Name : ")
student1 = Studentprofile(username, userid, userdep, useruni)
student2= Studentprofile(username2, userid2, userdep2, useruni2)
student1.student_profile()
print (f"Student last saw profile {current_datetime}")

student2.student_profile()
print (f"Student last saw profile {current_datetime}")
