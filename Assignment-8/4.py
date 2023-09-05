# class Cakes:
    
#     cake_price_per_kg = 1200
#     order_list = {}
#     feedback = {}
    
#     def __init__(self, flavor, weight):
#         self.flavor = flavor
#         self.weight = weight
#         self.sweetness = "Moderate sugar"
#         self.cream_type = "Whipped Cream"
#         self.customization = ""
#         self.price = self.cake_price_per_kg * (weight / 1000)
        
#         self.add_to_order_list()
    
#     def cake_details(self):
#         print(f"Flavor: {self.flavor} Cake, Weight: {self.weight} gm")
#         print(f"Sweetness: {self.sweetness}, Cream Type: {self.cream_type}")
#         print(f"Price: {self.price:.1f} Taka")
    
#     def add_to_order_list(self):
#         cake_key = f"{self.flavor} Cake {self.weight}gm"
#         if cake_key in self.order_list:
#             self.order_list[cake_key] += 1
#         else:
#             self.order_list[cake_key] = 1
    
#     def add_customization(self, sweetness="Zero", cream_type="Butter Cream"):
#         self.sweetness = sweetness
#         self.cream_type = cream_type
    
#     @classmethod
#     def give_feedbacks(cls, cake_flavor, feedback):
#         if cake_flavor in cls.feedback:
#             cls.feedback[cake_flavor].append(feedback)
#         else:
#             cls.feedback[cake_flavor] = [feedback]
            

    
#     @classmethod
#     def show_feedbacks(cls):
#         for flavor, feedbacks in cls.feedback.items():
#             print(f"{flavor}: {feedbacks}")
#             if "Cheese Cake" in flavor:
#                 print("You will get 10% discount for your next purchase!")


# class Cheese_Cakes(Cakes):
    
#     cake_price_per_kg = 1500
    
#     def __init__(self, flavor, weight, cake_type="Baked"):
#         super().__init__(flavor, weight)
#         self.cream_type = "Cream Cheese"
#         self.cake_type = cake_type
        
#         self.price = self.cake_price_per_kg * (weight / 1000)
#         self.customization = "Sorry! No customization available for cheese cakes."
    
#     def cake_details(self):
#         print(f"Flavor: {self.flavor} Cheese Cake, Weight: {self.weight} gm")
#         print(f"Sweetness: {self.sweetness}, Cream Type: {self.cream_type}")
#         print(f"Cake Type: {self.cake_type}, Price: {self.price:.1f} Taka")
    
#     def add_customization(self):
#         print(self.customization)
        
        
#     @classmethod
#     def give_feedbacks(cls, cake_flavor, feedback):
#         return super().give_feedbacks(cake_flavor, feedback)


# order_1=Cakes("Chocolate",500)
# order_2=Cakes("Vanilla",800)
# print("(1)**********************************")
# order_1.cake_details()
# print("(1.1)**********************************")
# print(Cakes.order_list)
# print("(2)**********************************")
# order_2.add_customization("Zero","Butter Cream")
# order_2.cake_details()
# print("(3)**********************************")
# Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
# Cakes.give_feedbacks("Chocolate Cake","Yummy")
# print("(4)**********************************")
# Cakes.show_feedbacks()
# print("(5)**********************************")
# ch_order1=Cheese_Cakes("Red velvet",700)
# ch_order1.cake_details()
# print("(6)**********************************")
# ch_order1.add_customization()
# print("(7)**********************************")
# ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
# ch_order2.cake_details()
# print("(8)**********************************")
# print(Cakes.order_list)
# print("(9)**********************************")
# Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
# Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
# print("(10)**********************************")
# Cakes.show_feedbacks()

class Cakes:
    order_list = {}
    feedbacks = {}

    def __init__(self, cake, weight):
        self.cake = cake
        self.weight = weight
        self.s = "Moderate"
        self.c = "Whipped Cream"
        key = f"{self.cake} Cake {self.weight}gm"
        if key not in Cakes.order_list.keys():
            Cakes.order_list[key] = 1
        else:
            Cakes.order_list[key] += 1

    def add_customization(self, s, c):
        self.s = s
        self.c = c

    def cake_details(self):
        print(f"Flavor: {self.cake} Cake, Weight: {self.weight}gm")
        print(f"Sweetness: {self.s} sugar, Cream Type: {self.c}")
        print(f"Price: {self.weight * 1.2} Taka")

    @classmethod
    def give_feedbacks(cls, flavor, feedback):
        print("Thanks for your valuable feedback!")
        if flavor not in cls.feedbacks:
            cls.feedbacks[flavor] = []
        cls.feedbacks[flavor].append(feedback)

    @classmethod
    def show_feedbacks(cls):
        print(cls.feedbacks)


class Cheese_Cakes(Cakes):
    def __init__(self, cake, weight, bake="baked"):
        super().__init__(cake, weight)
        self.bake = bake
        self.c = "Cream Cheese"

    def cake_details(self):
        print(f"Flavor: {self.cake} Cake, Weight: {self.weight}gm")
        print(f"Sweetness: {self.s} sugar, Cream Type: {self.c}")
        print(f"Cake Type: {self.bake}, Price: {self.weight * 1.5} Taka")

    def add_customization(self, s, c):
        print("Sorry! No customization available for cheese cakes.")

    @classmethod
    def give_feedbacks(cls, flavor, feedback):
        super().give_feedbacks(flavor, feedback)
        print("You will get 10% discount for your next purchase!")

    @classmethod
    def show_feedbacks(cls):
        super().show_feedbacks()


order_1 = Cakes("Chocolate", 500)
order_2 = Cakes("Vanilla", 800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero", "Butter Cream")
order_2.cake_details()
print("(3)**********************************")
Cakes.give_feedbacks("Chocolate Cake", "Very Delicious")
Cakes.give_feedbacks("Chocolate Cake", "Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1 = Cheese_Cakes("Red velvet", 700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization("Some", "Type")
print("(7)**********************************")
ch_order2 = Cheese_Cakes("Blue Berry", 900, "No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake", "Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake", "Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()
