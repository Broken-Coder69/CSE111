class Customer:
    def __init__(self, name):
        self.name = name
        self.dekhi_ki_ki_ase = []
        # self.abar_dekh_jadu = ""
        print(f"A customer named {self.name} has entered the store. ")
        
    def add_item(self, items):
        self.dekhi_ki_ki_ase = items

    
    def remove_item(self, shora_eida_bal):
        abar_dekh_jadu = []
        for i in self.dekhi_ki_ki_ase:
            if i != shora_eida_bal:
                abar_dekh_jadu.append(i)
            else:
                pass
        
        self.dekhi_ki_ki_ase = abar_dekh_jadu
        print(f"{shora_eida_bal} has been removed from the cart.")
            
    
    

    def shopping_details(self):
        eigulai_khali_ase = ",".join(self.dekhi_ki_ki_ase)
        return (f"{self.name} has the following items in the cart: \n{eigulai_khali_ase} ")



print("===================1===================")
customer1 = Customer("Sam")
print("===================2===================")
customer1.add_item(["Carrots", "Chips", "Rice"])
print("===================3===================")
print(customer1.shopping_details())
print("===================4===================")
customer1.remove_item("Carrots")
print("===================5===================")
print(customer1.shopping_details())




# ===================1=================== 
# A customer named Sam has entered the store. 
# ===================2=================== 
# ===================3=================== 
# Sam has the following items in the cart: 
# Carrots, Chips, Rice 
# ===================4=================== 
# Carrots has been removed from the cart. 
# ===================5=================== 
# Sam has the following items in the cart: 
# Chips, Rice
