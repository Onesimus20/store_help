"""from dataclasses import dataclass
class Smart_user:
    name:str
    age:int
    email:str = None
    last_login:int = 10


    def __init__(self,
                 name:str,
                 age:int,
                 email:str = None,
                 last_login:int = 10):
                 self.name = name
                 self.age = age
                 self.email = email
                 self.last_login = last_login
                 
                
other = Smart_user("Onesimus",21,1234567890)
other.name

nums = range(1,100)
def is_prime(num):
    for x in range(2,num):
        if (num % x) == 0:
            return False
    return True

prime = list(filter(is_prime, nums))
print(prime)

class Person:
    def __init__(self,
                 name):
        self.name = name

    def say_hello(self):x
        print("Hello {}!".format(self.name))
info = Person("Onesimus")
info.say_hello()





class Employer:
    def  __init__(self,
                  specification,
                  name,
                  age,
                  level,
                  salary):
        self.specification = specification
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
           
    def __str__(self):
        info = f"{self.name} is coding in Python laguage, At the age of years { self.age} receiving an Amount of ${self.salary}."
        return info   
        # print(f"{self.name} is coding in Python language,At the age of years { self.age} receiving an Amount of ${self.salary}.")

    def __str__(self):
        info = f"{self.name} is coding in Ruby laguage, At the age of years { self.age} receiving an Amount of ${self.salary}."
        return info
        
    def __eq__(self,other):  
        return self.age == other.age and self.name == other.name 
    


    @staticmethod
    def entery_salary(age):
        if age < 24:
            return 300
        if age <30:
            return 350
        return 500
    


list2 = Employer("CybersecurityEngine er","Wisdom","23","Senior",3500)
list3 = Employer("CybersecurityAnalyst","Maxwell","22","Senior",3000)
list4 = Employer("CybersecurityAnalyst","Maxwell","22","Senior",3000)
# list2.coding()
# print(list3.coding())
# list3.infomation("python")
print(Employer.entery_salary(24))
print(list2.entery_salary(27) )

print(list3)

print(list4 == list3)
joshua_number = 0530974239


@staticmethod
def entery_salary():
    age = [18,19,20,25,30,35]
    for Age in range(1,40):
        age = int(input("HOW OLD ARE YOU? "))
        if age == 25:
            return 250
        if age < 25:
            return 300
        if age > 25 and age <35:
            return 500
             print("{age} is out of the range. ")
             return None
        return "Your age is out of the range"
info = entery_salary()
print(info)

class Person:
    def __init__(self,
                 
                specification,
                name,
                age,
                level,
                salary):
        self.specification = specification
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    def __str__(self):
        info = f"{self.name} is coding in Ruby laguage, At the age of years { self.age} receiving an Amount of ${self.salary}."
        return info
result = Person("CybersecurityEngineer","Wisdom","23","Senior",3500)
print(result)
"""


"""class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def is_working(self):
        print(f"{self.name} is working at age {self.age} years old as a SoftwareEngineer.")

class B(A):
    pass

class C(A):
    pass

SE = A("Onesimus",21)
CA =B("Maxwell",22)
WD =C("Rejoice",23)
SE.is_working()
CA.is_working()
WD.is_working()
""" 
"""class Custosmer:
    def __init__(self,Name,
                 staffID,
                 customer_department):
        self.name = Name
        self.customerID = staffID
        self.customer_department = customer_department
class QualityControl(Custosmer):
    def __init__(self, Name, customerID, customer_department):
        super().__init__(Name, customerID, customer_department)


    def parkaging(self):
        print("Here we do parking.")

com = Custosmer("Onesimus",206485,"quality_control")
com.customer_department"""


#Bank Operation Using OOP

from typing import Self


class Bank:
    bankname = "Quantum Express Bank"
    branch = "Teleku-Bokazo, Opposite Kamps Garden, TER235 Third floor."

    #creating Account
    def __init__(self,username,pan,address):
        self.username = username
        self.pan = pan
        self.address = address
        self.intial_balance = 0.00

        print(f"Hello {self.username} congratulation! Your Account Has Been successfully Created. ")

    def deposite(self,amount):
        self.intial_balance = self.intial_balance + amount
        print(f"{amount} deposited  sucessfully.")

    def ministatement(self):
        print(f"Your Current Balance is $ {self.intial_balance}. ")

    def withdraw(self,amount):
        
        # withdraw = float(input("Enter Amount You want To Withdraw. "))
        if withdraw < self.intial_balance:
            self.intial_balance = self.intial_balance - amount
            print(f"An amount of $ {withdraw} has been withdraw from your account.")
        else:
            print("Insufficient Balance")  
          
            # print(self.intial_balance)
        

print(f"Welcome To {Bank.bankname}, our offices are open to our client, our Headquaters is at {Bank.branch} And it's open at any point in time.")
username = input("Enter Your Name. ")
pan = input("Enter Your PAN card number. ") 
address = input("Enter Your Address. ")

b = Bank(username,pan,address)


while True:
    print("Please Select any option. ")
    print("1.Deposite\n2.Withdraw\n3.Ministatement\n4.stop")
    option = int(input(" Option...  "))
    if option==1:
        # print("How Much Do You Want To Deposite ? ")
        amount = float(input("How Much Do You Want To Deposite? $"))
        # if amount < amount.intial_balance:
        #     print("Your Deposite Must Be Greater than 0.00")
        # else:
        """print(f"${amount} is succefully deposited")
        print(f"You Current Balance is ${amount}")"""
        b.deposite(amount)
        
    elif option == 2:
        withdraw = float(input("How Much Do You Want To Withdraw? $"))
        b.withdraw(withdraw)
        # print("How Much Do You Want To Withdraw ? ")
        """if withdraw < amount:
            print("Insufficient Balance")
        else:
            print(self.intial_balance)"""

    elif option == 3:
        b.ministatement()

    elif option == 4:
        print("Thank You for using Quantum Express.")
        break
    else:
        print("INVALID INPUT PLEASE SELECT A VALID OPTION")
"""b.deposite(amount)
b.withdraw(amount)""" 