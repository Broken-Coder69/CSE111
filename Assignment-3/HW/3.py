class box:
    def __init__(self, msr_list):
        self.height = msr_list[0]
        self.width = msr_list[1]
        self.breadth = msr_list[2]
        print("Creating a Box!")




print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
volume = b1.height * b1.width * b1.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
volume = b3.height * b3.width * b3.breadth
print(f"Volume of the box is {volume} cubic units.")
