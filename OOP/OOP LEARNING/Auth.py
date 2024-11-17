class Authentication:
    def __init__(self,username,password,email,phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
name = input("Enter Your Name : ")
password = input("Enter Your Password : ")
email = input("Enter your mail : ")
phone = (input("Enter your phone number : "))
Auth = Authentication(name, password, email, phone)
print(f"The name is {Auth.username} password is {Auth.password} email is {Auth.email} and phone number is {Auth.phone}",)


     