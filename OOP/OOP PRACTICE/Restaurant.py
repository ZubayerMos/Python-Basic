class Restaurant ():
    def __init__(self, rice,soup,chicken,beef,vegetable ) :
        self.rice = rice
        self.soup = soup
        self.chicken = chicken
        self.beef = beef
        self.vegetable = vegetable
        
print ("For searching")

customer_rice = input("Enter Your Rice Choice : ")
customer_soup = input("Enter Your Soup Choice : ")
customer_chicken = input("Enter Your Chicken Choice : ")
customer_beef = input("Enter Your Beef Choice : ")
customer_vegetable = input("Enter Your Vegetable Choice :")

Customer_choice = Restaurant(customer_rice, customer_soup, customer_chicken, customer_beef, customer_vegetable)    

print (f"Customer Rice choice is {Customer_choice.rice}\n ")  
print (f"Customer Soup choice is {Customer_choice.soup}\n ")  
print (f"Customer Chicken choice is {Customer_choice.chicken}\n ")
print (f"Customer Beef choice is {Customer_choice.beef}\n ")
print (f"Customer Vegetable choice is {Customer_choice.vegetable}\n ")