class CoffeeMachine:
    def __init__(self, name):
        self.name = name
        self.items = ""
        
        
    def insertIngredients(self, *args):
        if args:
            self.items = ", ".join(args)

    
    
    def getDetails(self):
        print(f"Brand Name: {self.name}")
        return f"Ingredients: {self.items}"


cm1 = CoffeeMachine("Miyako")
cm1.insertIngredients("Coffee beans", "Milk", "Sugar")
print(cm1.getDetails())


# Output:
# Brand Name: Miyako
# Ingredients: Coffee beans, Milk, Sugar