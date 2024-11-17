class Library ():
    def __init__(self, admin,password, id) :
        self.admin = admin
        self.password = password
        self.id = id
print ("for admin")
useradmin = input("Enter admin name : ")
adpass = input("Enter a password : ")
adid = input("Enter admin Id : ")
libadmin = Library(useradmin, adpass, adid)
print (f"Admin name is {libadmin.admin}")
print (f"Admin password is {libadmin.password}")
print (f"Admin id is {libadmin.id}\n")

print ("For Book")
class Book ():
    def __init__(self, name, department, price):
        self.name = name
        self.department = department
        self.price = price
bookname = input("Enter Book name : ")
book_dep = input("Enter book department : ")
book_price = input("Enter Book price : ")
libBOOk = Book(bookname, book_dep, book_price)
print (f"Book name is {libBOOk.name}")
print (f"Book department is {libBOOk.department}")
print (f"Book price is {libBOOk.price}\n")

print ("For Author\n")

class Author ():
    def __init__(self,name, department, book_name):
        self.name = name
        self.department = department
        self.book_name = book_name
authorname = input("Enter Author name : ")
authordep = input("Enter Author department : ")
author_book = input("Enter Book name :")
auth_info = Author(authorname, authordep, author_book)
print (f"Author name is {auth_info.name} ")
print (f"Author department is {auth_info.department} ")
print (f"Author book is {auth_info.book_name} ")

print("For Customer\n")

class Customer ():
    def __init__(self, name, password, buy_book):
        self.name = name
        self.password =password
        self.buy_book = buy_book
cus_name = input("Enter Customer Name : ")
cus_pass = input("Enter Your Password : ")
cus_book = input("Buy your favourtie book : ")
cus_info = Customer(cus_name, cus_pass, cus_book)
print (f"Customer name is {cus_info.name}")
print (f"Customer pass is {cus_info.password}")
print (f"Customer book is {cus_info.buy_book}")

print ("for signup")
class Signup():
    def __init__(self, name,email, password):
        self.name = name
        self.email = email
        self.password = password
signname = input("Enter your name : ")
signmail = input("Enter your email : ")
signpass = input("Enter your password : ")
signid = Signup(signname, signmail, signpass)
print (f"Customer name is {signid.name} ")
print (f"Customer mail is {signid.email} ")
print (f"Customer password is {signid.password} ")

if cus_info.name == signid.name and cus_info.password== signid.password :
    print ("Account Created Successfully!")
else :
    print ("Error password.Try Again.")
        