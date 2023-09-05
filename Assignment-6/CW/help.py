class NikeBangladesh:
    # Class variable to keep track of all branches
    branches_opened = []

    def __init__(self, place):
        self.place = place
        self.stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        self.sold = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        NikeBangladesh.branches_opened.append(place)

    def status(self):
        print("Nike Bangladesh Status:")
        print("Branches Opened:", NikeBangladesh.branches_opened)
        print("Currently Stocked")
        print(self.stock)
        total_sold = 0
        for quantity in self.sold.values():
            total_sold += quantity
        print("Sold:", total_sold)

    def restockProducts(self, products):
        for product, quantity in products.items():
            self.stock[product] += quantity

    def details(self):
        print(f"Nike {self.place} outlet:")
        print("Products Currently Stocked:")
        print(self.stock)
        total_sold = 0
        for quantity in self.sold.values():
            total_sold += quantity
        print("Sold:", total_sold)

    def productSold(self, products):
        for product, quantity in products.items():
            if product in self.stock and self.stock[product] >= quantity:
                self.stock[product] -= quantity
                self.sold[product] += quantity
            else:
                print(f"Not enough {product} in stock at {self.place}")


print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
