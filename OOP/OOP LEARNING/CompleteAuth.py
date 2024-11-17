class Authentication:
    def __init__(self,username,password,email,phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
print ("For SignUp")
name = input("Enter Your Name : ")
password = input("Enter Your Password : ")
email = input("Enter your mail : ")
phone = (input("Enter your phone number : "))
Auth = Authentication(name, password, email, phone)

print ("For Login")
name = input("Enter Your userName : ")
password = input("Enter Your Password : ")
if name == Auth.username and password == Auth.password :
    print ("Login Successful")
    print ("User Dashboard ")
    print (f"Hi {Auth.username}")
    print (f"email is : {Auth.email}")
    print (f"phone number is : {Auth.phone}")
else :
    print ("Login Failed")

     