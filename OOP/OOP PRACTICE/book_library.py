class Book_library():
    def __init__(self,name,author_name,price,stall) :
        self.name = name
        self.author_name = author_name
        self.price= price
        self.stall = stall
book_name = input("Enter Book Name : ")
authorname = input("Enter Author name : ")
price_book = input ("Enter book price :  ")
stallname = input ("Enter Stall name : ")
New_book_library = Book_library(book_name,authorname,price_book,stallname)
print (f"Book name is {New_book_library.name}\n Book Author name is {New_book_library.author_name}\n Book price is {New_book_library.price}\n Book stall name is {New_book_library.stall}\n")