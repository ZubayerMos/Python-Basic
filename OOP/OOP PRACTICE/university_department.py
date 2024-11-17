class University_department ():
    def __init__(self, CSE,EEE,DS,ML,BBA):
        self.CSE = CSE
        self.EEE= EEE
        self.DS = DS
        self.ML= ML
        self.BBA = BBA
up_cse = input("Enter Department Name : ")
up_eee = input("Enter Department Name : ")
up_DS = input("Enter Department Name : ")
up_ML = input("Enter Department Name : ")
up_BBA = input("Enter Department Name : ")
up_uni_dep = University_department(up_cse,up_eee,up_DS,up_ML,up_BBA)
print (f"University department is {up_uni_dep.CSE}\n University department is {up_uni_dep.EEE}\n University department is {up_uni_dep.DS}\n University department is {up_uni_dep.ML}\n University departmdent is {up_uni_dep.BBA}\n ")
 
if up_uni_dep.CSE == up_cse:
    print ("Admission fee is 1039500")
if up_uni_dep.EEE == up_eee:
    print ("Admission fee is 10,25000")
if up_uni_dep.DS == up_DS:
    print ("Semester fee is 9,90000")
if up_uni_dep.ML == up_ML:
    print ("Semester fee is 9,80000")
if up_uni_dep.BBA == up_BBA:
    print ("Semester fee is 9,70000")
else :
    print ("Write a exact Department")
    