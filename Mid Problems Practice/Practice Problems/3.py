class Building:
    def __init__(self, name, company):
        self.name = name 
        self.company = company
        self.dict = {}
        

    def constructBuilding(self, location, area, price):
        total_cost = area * price
        print(total_cost)
   

    
    def details(self):
        print(f"{self.name} is a {self.company} company ")




bti = Building('bti', 'Real Estate')
bti.constructBuilding('Mohakhali', 1500, 6000)
bti.constructBuilding('Lalmatia', 1500, 8000)
print("===================1===================")
bti.details()


# ===================1=================== 
# bti is a Real Estate company 
# Building1 is in location: Mohakhali 
# Its total cost is: 9000000 
# Building2 is in location: Lalmatia 
# Its total cost is: 12000000