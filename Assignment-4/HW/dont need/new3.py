class Farmer:
    def __init__(self, name="Welcome to your farm!"):
        self.name = name
        self.crops = []
        self.fishes = []
        

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

    # def __str__(self):
    #     return f"Welcome to your farm. Your farm ID is {self.name}!"


# Test the code
f1 = Farmer()
print(f1)
print("-------------------")
f1.addCrops('Rice', 'Jute', 'Cinnamon')
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print(f2)
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
print(f3)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")