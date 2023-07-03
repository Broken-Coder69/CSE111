# You are the proud owner of a mangoficent mango orchard where you have different varieties of mango trees such as Fazlee, Langda, 
# Harivanga, Himsagar, etc. But this year, demand for Gopalbhog and Amrapali is too high. To cater to this unsatisfied demand in the future, 
# you have decided to plant these two varieties in your orchard. 

# (i) Now, based on the given driver code, you need to design a MangoTree class. 
# Initially, when you plant a tree, it will have a height of 1 meter and the number of mangoes will be 0. 



class MangoTree:
    def __init__(self, variety):
        
        self.variety = variety
        self.height = 1
        self.number_of_mangoes = 0






mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")
