# class Order:
#     def __init__(self, menu, order_string):
#         self.menu = menu
#         self.items = self.parse_order(order_string)

#     def parse_order(self, order_string):
#         items = order_string.split(', ')
#         parsed_items = []
#         for item in items:
#             item_name, quantity = item.split('-')
#             parsed_items.extend([item_name.strip(), int(quantity), self.menu.get(item_name.strip(), 0) * int(quantity)])
#         return parsed_items

#     def calculate_total(self):
#         total = 0
#         for index in range(2, len(self.items), 3):
#             total += self.items[index]
#         return total



# class Order:
#     def __init__(self, menu, order_string):
#         self.menu = menu
#         self.items = []
#         self.total = 0
        
#         items = order_string.split(', ')
#         for item in items:
#             item_info = item.split('-')
#             item_name = item_info[0].strip()
#             quantity = int(item_info[1])
#             price = self.menu.get(item_name, 0) * quantity
#             self.items.extend([item_name, quantity, price])
#             self.total += price


class Order:
    def __init__(self, menu, order_string):
        self.menu = menu
        self.items = []
        self.total = 0
        
        items = order_string.split(', ')
        for item in items:
            item_info = item.split('-')
            item_name = item_info[0].strip()
            quantity = int(item_info[1])
            if item_name in self.menu:
                price = self.menu[item_name] * quantity
            else:
                price = 0
            self.items.extend([item_name, quantity, price])
            self.total += price


menu = {
'Chicken_Cheeseburger' : 249,
'Mega_Cheeseburger' : 289,
'Fries' : 139,
'Hot_Wings' : 99,
'Rice_Bowl' : 299,
'Soft_Drinks' : 50
}
order1 = Order(menu, "Chicken_Cheeseburger-2, Fries-3, Soft_Drinks-3")
print(order1.items)
print()
print('-'*35)
print('Item x Quantity : Price')
print('-------------- -------- -------')
index = 0
total = 0
while index < len(order1.items):
    item = order1.items[index]
    quantity = order1.items[index+1]
    price = order1.items[index+2]
    print(f'{item:20} x {quantity:2} : {price:7.2f}')
    total += price
    index += 3 # Going to next item
print('-'*35)
print(f'Total:                       {total:7.2f}')
print('-'*35)
