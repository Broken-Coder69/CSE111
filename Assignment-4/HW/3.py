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



