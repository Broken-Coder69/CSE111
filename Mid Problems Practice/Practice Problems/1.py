class Customer:
    def __init__(self, name):
        self.name = name
        print(f"A customer named {self.name} has entered the store.")
        self.items_str = ""
        
    def add_item(self, items):
        self.items_str = ",".join(items)
    
    def shopping_details(self):
        return f"{self.name} has the following items in the cart: \n{self.items_str}" 






print("===================1===================")
customer1 = Customer("Sam")
print("===================2===================")
customer1.add_item(["Carrots", "Chips", "Rice"])
print("===================3===================")
print(customer1.shopping_details())
print("===================4===================")
customer2 = Customer("Bob")
print("===================5===================")
customer2.add_item(["Oats", "Apples"])
print("===================6===================")
print(customer2.shopping_details())


# ===================1=================== 
# A customer named Sam has entered the store. 
# ===================2=================== 
# ===================3=================== 
# Sam has the following items in the cart: 
# Carrots, Chips, Rice 
# ===================4=================== 
# A customer named Bob has entered the store. 
# ===================5=================== 
# ===================6=================== 
# Bob has the following items in the cart: 
# Oats, Apples






