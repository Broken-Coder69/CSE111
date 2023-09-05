class UniversalStudiosUser:
    def __init__(self, name, age, category):
        self.name = name
        self.age = age
        self.category = category
        self.ride = []
        self.price = []
        self.total = 0
        print("Welcome to Universal Studios.")
        
    def selected_rides(self, *rides):
        if rides:
            print("Added ride(s) successfully")
            for i in rides:
                ride, amount = i.split("-")
                self.ride.append(ride)
                self.price.append(amount)
                self.total += float(amount)
                

    
    def show_details(self):
        print("Your information:")
        print(f"Name: {self.name}, Age: {self.age}, Category: {self.category}")
        print("Selected rides:")
        for i in range(len(self.ride)):
            print(f"Ride: {self.ride[i]}, Amount: {self.price[i]} dollar(s)")
        
        if self.category == "Special" and len(self.ride) > 3:
            discount = (self.total * 20) / 100
            offer_price = self.total - discount
            print(f"Congratulations!!! You've got a 20% discount. Please pay {float(offer_price)} dollar(s).")
        else:
            print(f"Please pay {self.total} dollar(s).")




# Lucky winners (Special users) get a 20% discount if they select more than 3
# rides. Normal users do not get any discounts.


# Your information:
# Name: Alice, Age: 21, Category: Special
# Selected rides:
# Ride: Waterworld, Amount: 100 dollar(s)
# Ride: Accelerator, Amount: 200 dollar(s)
# Ride: DinoSoarin, Amount: 50 dollar(s)
# Please pay 350.0 dollar(s).








customer_1 = UniversalStudiosUser("Alice", 21,
"Special")
print("--------- 1 ---------")
customer_1.selected_rides("Waterworld-100",
"Accelerator-200", "DinoSoarin-50")
print("--------- 2 ---------")
customer_1.show_details()
print("=================")
customer_2 = UniversalStudiosUser("Bob", 20,
"Normal")
print("--------- 3 ---------")
customer_2.selected_rides("Enchanted Airways-300",
"Jurassic Park-500", "Accelerator-200",
"DinoSoarin-50")
print("--------- 4 ---------")
customer_2.show_details()
print("=================")
customer_3 = UniversalStudiosUser("Mark", 15,
"Special")
print("--------- 5 ---------")
customer_3.selected_rides("Transformers-450",
"Jurassic Park-500", "Waterworld-100",
"DinoSoarin-50")
print("--------- 6 ---------")
customer_3.show_details()
