class PizzaMachine:
    def __init__(self, name = "regular", size = 6):
        self.name = name
        self.size = size

    def customizePizza(self, toppings, spice_level="Regular"):
        # topping_items = ""
        
        
        if spice_level == "Regular" or spice_level == "Hot" or spice_level == "Super Naga":
            if type(toppings) == list:
                # for i in toppings:
                toppings_str = ",".join(toppings)
                return f"Your {self.size}-inch {spice_level} spicy {self.name} Pizza is ready with {toppings_str} toppings. Enjoy!"
            else:
                return f"No toppings specified! Can't bake pizza."
        else:
            return f"Sorry! Spice level not allowed. Can't bake pizza."
        
    
    


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



# 1#################################
# Your 6-inch Hot spicy Regular Pizza is ready with
# Cheese,Pepperoni toppings. Enjoy!
# 2================================
# 3#################################
# No toppings specified! Can't bake pizza.
# 4================================
# 5#################################
# Your 12-inch Regular spicy Chicken Blast Pizza is ready
# with Mushroom toppings. Enjoy!
# 6================================
# 7#################################
# Sorry! Spice level not allowed. Can't bake pizza.
# 8================================

