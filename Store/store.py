"""while True:
  def shop():
    name = input("Enter Name of The shop. ")
    print(f"Thanks for choosing {name}.. ")

  def items ():
    name = input("Enter Your Name.")
    print(f"Welcome To {name} cosmestics, here we sell good and power cosmetics.")
  

    item = input("What Do You Want To Buy?. ")
    product = ["CocoButter","Lulu","PerfectWhite","BioClear","BioSkin"]
    if item in product:
      price:float = 23.34
      print(f"The Price of product  is ${price}. ")
    else:
      print("If We Dont Have Such a Product.")

    print("1.CocoButter\n2.Lulu\n3.PerfectWhite\n4.BioClear\n5.BioSkin") 
    instructions = int(input("What Do You Want To Buy? "))
    if instructions == 1 and product[0]:
      price:float = 23.34
      print(f"The Price of {product[0]} is ${price}. ")
    
    elif instructions == 2:
      price:float = 25.30
      print(f"The Price of {product[1]} is ${price}. ")

    elif instructions == 3:
      price:float = 15.30
      print(f"The Price of {product[2]} is ${price}. ")

    elif instructions == 4:
      price:float = 20.00
      print(f"The Price of {product[3]} is ${price}. ")

    elif instructions == 5:
      price:float = 5.30
      print(f"The Price of {product[4]} is ${price}. ")
    else:
      print("INVALID INPUT")

  shop()
  items()
  break """

# class Shop:
#   shop_name = "Cosmos Cosmetics"
#   location = "Teleku-Bokazo, opposite Frycool computers."

#   def __init__(self,name):
#     name = input("Enter The Customer Name. ")
#     self.name = name
    
#   def welcome_message(self,name):
#     self.name = name
#     print(f"Welcome, dear {self.name} Thanks choosing {Shop.shop_name}. How may I help you.")

# print(f"Welcome to {Shop.shop_name} we're located at {Shop.location}. ")



# b = Shop("kokoo")
# b.welcome_message
