class Student_information():
    def __init__(self, name, id, mail, password,phone,avg_cgpa) :
        self.name = name
        self.id = id
        self.mail = mail
        self.password = password
        self.phone = phone
        self.cgpa = avg_cgpa
username = input("Enter your Name : ")
userid = input("Enter your id : ")
usermail = input("Enter your mail : ")
userpassword = input("Enter your password : ")
userphone = input("Enter your Phone Number : ")
useravgcgpa = input("Enter your avg cgpa : ")
Current_information = Student_information(username, userid, usermail, userpassword,userphone,useravgcgpa)
print (f"Student name is {Current_information.name}\n Student id is {Current_information.id}\n Student mail is {Current_information.mail}\n Student password is {Current_information.password}\n Student phone number is {Current_information.phone}\n Student average cgpa is {Current_information.cgpa}\n")