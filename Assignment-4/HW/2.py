# class Foodie:
#     def __init__(self, name):
#         self.name = name
#         self.orders = []
#         self.total_spent = 0

#     def show_orders(self):
#         print(f"{self.name} has {len(self.orders)} item(s) in the cart.")
#         print("Items:", self.orders)
#         print("Total spent:", self.total_spent)

#     def order(self, *items):
#         for item in items:
#             food, quantity = item.split('-')
#             if food in menu:
#                 price_per_unit = menu[food]
#                 total_price = price_per_unit * int(quantity)
#                 self.orders.append(food)
#                 self.total_spent += total_price
#                 print(f"Ordered - {food}, quantity - {quantity}, price (per Unit) - {price_per_unit}.")
#                 print("Total price -", total_price)

#     def pay_tips(self, tips=0):
#         if tips > 0:
#             print(f"Gives {tips}/- tips to the waiter.")
#         else:
#             print("No tips to the waiter.")


class Foodie:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.total_spent = 0
        
    def show_orders(self):
        print(f"{self.name} has {len(self.orders)} item(s) in the cart.")   
        print(f"Items: {self.orders}")
        print(f"Total spent: {self.total_spent}.")
        return ""
    
    def order(self, *items):                                                         
        for i in items:                                     
            food, quantity = i.split("-")                                   
            if food in menu:
                price = menu[food]
                total_price = price * int(quantity)
                self.orders.append(food)
                self.total_spent += total_price
                print(f"Ordered - {food}, quantity - {quantity}, price (per Unit) - {price}.")
                print(f"Total price - {total_price}")

    
    
    def pay_tips(self, tips=0):
        if tips == 0:
            print(f"No tips to the waiter.")
        else:
            print(f"Gives {tips}/- tips to the waiter.")






menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}
f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())


# Frodo has 0 item(s) in the cart.
# Items: []
# Total spent: 0.
# 1----------------------
# Ordered - Chicken Lollipop, quantity - 3, price (per
# Unit) - 15.
# Total price - 45
# Ordered - Beef Nugget, quantity - 6, price (per Unit)-
# 20.
# Total price - 120
# Ordered - Americano, quantity - 1, price (per Unit)-
# 180.
# Total price - 180
# 2----------------------
# Frodo has 3 item(s) in the cart.
# Items: ['Chicken Lollipop', 'Beef Nugget',
# 'Americano']
# Total spent: 345.
# 3----------------------
# Ordered - Red Velvet, quantity - 1, price (per Unit)-
# 150.
# Total price - 150
# 4----------------------
# Gives 20/- tips to the waiter.
# 5----------------------
# Frodo has 4 item(s) in the cart.
# Items: ['Chicken Lollipop', 'Beef Nugget',
# 'Americano', 'Red Velvet']
# Total spent: 515.
# 6----------------------
# Ordered - Prawn Tempura, quantity - 6, price (per
# Unit)- 80.
# Total price - 480
# Ordered - Saute Veg, quantity - 1, price (per Unit)-
# 200.
# Total price - 200
# 7----------------------
# No tips to the waiter.
# 8----------------------
# Bilbo has 2 item(s) in the cart.
# Items: ['Prawn Tempura', 'Saute Veg']
# Total spent: 680.