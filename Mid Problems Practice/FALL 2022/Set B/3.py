class PizzaMachine:
    def __init__(self, pizza="Regular", size=6):
        self.pizza = pizza
        self.size = size 


    def customizePizza(self, toppings, spice_level="Regular"):
        if type(toppings) == list:
            # if toppings:
            topping_items = ",".join(toppings[0:])
            if spice_level == "Regular" or spice_level == "Super Naga" or spice_level == "Hot":
                return f"Your {self.size}-inch {spice_level} spicy {self.pizza} Pizza is ready with {topping_items} toppings. Enjoy!"
            else:
                return f"Sorry! Spice level not allowed. Can't bake pizza"
        else:
            return f"No toppings specified! Can't bake pizza."




pizza1 = PizzaMachine()
order1 = pizza1.customizePizza(["Cheese", "Pepperoni"],"Hot")
print("1################################# ")
print(order1)
print("2================================")

pizza2 = PizzaMachine("Vege")
order2 = pizza2.customizePizza("Super Naga")
print("3#################################")
print(order2)
print("4================================")
pizza3 = PizzaMachine("Chicken Blast",12)

order3 = pizza3.customizePizza(["Mushroom"])
print("5#################################")
print(order3)
print("6================================")

pizza4 = PizzaMachine("Beef Bonanza",16) 
order4 = pizza4.customizePizza(["Cheese","Beef kala bhuna"],"Mild")
print("7#################################")
print(order4)
print("8================================")
