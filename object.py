class Bank:
  BankName = "MY0HAUNG EXPRESS BANK."
  BankBranch = "DUBLIN office room_no.  23A, Third floor."
  

  def __init__(self,name,age,card_number,location):
    self.name = name
    self.age = age
    self.card_number = card_number
    self.location = location
    self.balance = 5.00

  """def accont_creation(self):
    self.name = name
    self.age = age
    self.card_number = card_number
    self.location = location"""
  
  def deposite(self,amount):
    self.balance = self.balance + amount



print(f"Welcome To {Bank.BankName} we're located at {Bank.BankBranch} we're ready to service you. ")
AGE = 18
name = input("Enter your name.")
location = input("Enter Your Location..")
age = int(input("Enter Your Age. "))
card = ["1.Ghana_card\n2.NHIS\n3.Student_card"]
if card == 1 and age < AGE:
  print("ACCOUNT CREATED SUCCESSFULLY.. ")
else:
  print("YOU ARE NOT QUALIFY TO CREATE AN ACCOUNT.")
  pass  

b = Bank(name,age,card,location)
b.deposite(2344)
# print("Select ID..")



"""
card = ["1.Ghana_card\n2.NHIS\n3.Student_card"]
if card == 1 and age < AGE:
  print("ACCOUNT CREATED SUCCESSFULLY.. ")
else:
  print("SORRY! YOU ARE NOT QUALIFY TO CREATE AN ACCOUNT BECAUSE YOU ARE UNDER AGE!, THANKS FOR CHOSING MYOHAUG EXPRESS. ")
  # continue
if card == 1 and age > AGE:
  print("SUCCESSFUL")
else:
  print("ACCOUNT CREATION DENIED")"""



while True:
     
   card = {1: "Ghana_card",
           2: "NHIS",
           3: "Student_card"}
   print("Select ID..",card)
   card = input("Select an option..")
   for cards in card:
    if card == card[0] and age > AGE:
      print("ACCOUNT CREATED SUCCESSFULLY.. ")

    while True:
      print("Please Select any option. ")
      print("1.Deposite\n2.Withdraw\n3.Ministatement\n4.stop")
      option = int(input(" Option: ==> "))
      if option==1:
          # print("How Much Do You Want To Deposite ? ")
          amount = float(input("How Much Do You Want To Deposite? $"))
          # if amount < amount.intial_balance:
          #     print("Your Deposite Must Be Greater than 0.00")
          # else:
          print(f" Dear customer an amount of ${amount} has been succefully deposited into your Account.")
          print(f"Your Current Balance is ${amount}")

          while True:
             print("1.Exit\n2.Withdraw\n3.Back To Main Menu\n4.stop")
             user_option = int(input("Enter an option. "))
             if user_option == 1:
                break

             elif user_option == 3:
                print("1.Deposite\n2.Withdraw\n3.Ministatement\n4.stop")
          
      if option == 2:
          withdraw = float(input("How Much Do You Want To Withdraw? $"))
          # print("How Much Do You Want To Withdraw ? ")
          if withdraw < self.balance:
              print("Insufficient Balance")
          else:
              print(amount)
      if option == 3:
         print("1.Deposite\n2.Withdraw\n3.Ministatement\n4.stop")
      else:
         print("none")

      if option == 4:
          print("Thank You for using Quantum Express.")
          break
  
  #   elif age < AGE:
  #       print("YOU ARE NOT QUALIFY TO CREATE AN ACCOUNT. ")
  #   else:
  #       print("ACCOUNT CREATED SUCCESSFULLY.")

  #  AGE = 18
  #  name = input("Enter your name.")
  #  age = int(input("Enter Your Age. "))

  #  location = input("Enter Your Location..")
