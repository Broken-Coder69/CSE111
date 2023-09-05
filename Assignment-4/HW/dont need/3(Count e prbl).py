# # class Farmer:
# #     def __init__(self, *args):
# #         self.args = args
# #         self.alpha = "qwertyuiopasedfghjklzxcvbnm"
# #         self.count = 0  
# #         if len(args) == 0:
# #             print("Welcome to your farm!")
# #         else:
# #             name = str(self.args[0])
# #             for i in name:
# #                 if i in self.alpha:
# #                     self.count += 1               
# #             if self.count > 0:
# #                 print(f"Welcome to your farm, {name}!")
# #             else:
# #                 print(f"Welcome to your farm. Your farm ID is {name}!")
                
# #         self.crops = []
# #         self.crops_count = 0
# #         self.fishes = []
# #         self.fish_count = 0        
        
        
# #     # def addCrops(self, *crops):
# #     #     if crops:
# #     #         self.crops.extend(crops)
# #     #         self.crops_count += 1
# #     #         print(f"{len(crops)} crop(s) added.")
# #     #     else:
# #     #         print("No crop(s) added.")
            
# #     def addCrops(self, *crops):
# #         if crops:
# #             self.crops.extend(crops)
# #             print(f"{len(crops)} crop(s) added.")
# #         else:
# #             print("No crop added.")   
    
    
# #     def addFishes(self, *fishes):
# #         if fishes:
# #             self.fishes.extend(fishes)
# #             print(f"{len(fishes)} fish(s) added.")
# #         else:
# #             print("No fish added.")   
    
    
#     # def addFishes(self, *fishes):
#     #     if fishes:
#     #         self.fishes.extend(fishes)
#     #         print(f"{len(fishes)} fish(s) added.")
#     #     else:
#     #         print("No fish added.")
    


# # You have 4 crop(s):
# # Rice,Jute,Cinnamon,Mustard
# # You don't have any fish(s).








#     def showGoods(self):
#         if self.crops:
#             print(f"You have {self.crops_count} crop(s)")
#         else:
#             print("You don't have any crop(s).")

#         if self.fishes:
#             print(f"You have {len(self.fishes)} fish(s)")
#         else:
#             print("You don't have any fish(s).")

            
            
            
            
                                                                           










# f1 = Farmer()
# print("-------------------")
# f1.addCrops('Rice', "Jute", "Cinnamon")
# print("-------------------")
# f1.addFishes()
# print("-------------------")
# f1.addCrops('Mustard')
# print("-------------------")
# f1.showGoods()
# print("-------------------")
# f2 = Farmer("Korim Mia")
# print("-------------------")
# f2.addFishes('Pangash', 'Magur')
# print("-------------------")
# f2.addCrops("Wheat", "Potato")
# print("-------------------")
# f2.addFishes("Koi", "Tuna", "Sardine")
# print("-------------------")
# f2.showGoods()
# print("-------------------")
# f3 = Farmer(2865127000)
# print("-------------------")
# f3.addCrops()
# print("-------------------")
# f3.addFishes("Katla")
# print("-------------------")
# f3.showGoods()
# print("-------------------")


# # Welcome to your farm!
# # -------------------
# # 3 crop(s) added.
# # -------------------
# # No fish added.
# # -------------------
# # 1 crop(s) added.
# # -------------------
# # You have 4 crop(s):
# # Rice,Jute,Cinnamon,Mustard
# # You don't have any fish(s).
# # -------------------
# # Welcome to your farm, Korim Mia!
# # -------------------
# # 2 fish(s) added.
# # -------------------
# # 2 crop(s) added.
# # -------------------
# # 3 fish(s) added.
# # -------------------
# # You have 2 crop(s):
# # Wheat,Potato
# # You have 5 fish(s):
# # Pangash,Magur,Koi,Tuna,Sardine
# # -------------------
# # Welcome to your farm. Your farm ID
# # is 2865127000!
# # -------------------
# # No crop(s) added.
# # -------------------
# # 1 fish(s) added.
# # -------------------
# # You don't have any crop(s).
# # You have 1 fish(s):
# # Katla
# # -------------------





class Farmer:
    def __init__(self, *args):
        self.args = args
        self.alpha = "qwertyuiopasedfghjklzxcvbnm"
        self.count = 0
        if len(args) == 0:
            print("Welcome to your farm!")
        else:
            name = str(self.args[0])
            for i in name:
                if i in self.alpha:
                    self.count += 1
            if self.count > 0:
                print(f"Welcome to your farm, {name}!")
            else:
                print(f"Welcome to your farm. Your farm ID is {name}!")

        self.crops = []
        self.crops_count = 0
        self.fishes = []
        self.fish_count = 0


    def addCrops(self, *crops):
        if crops:
            self.crops.extend(crops)
            print(f"{len(crops)} crop(s) added.")
        else:
            print("No crop added.")


    def addFishes(self, *fishes):
        if fishes:
            self.fishes.extend(fishes)
            print(f"{len(fishes)} fish(s) added.")
        else:
            print("No fish added.")



    def showGoods(self):
        if self.crops:
            print(f"You have {len(self.crops)} crop(s):\n{','.join(self.crops)}")
        else:
            print("You don't have any crop(s).")

        if self.fishes:
            print(f"You have {len(self.fishes)} fish(s):\n{','.join(self.fishes)}")
        else:
            print("You don't have any fish(s).")



f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")



