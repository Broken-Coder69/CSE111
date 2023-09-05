class Student:
    def __init__(self, name, id, cg):
        self.name = name
        self.id = id
        self.cg = cg    
        self.id_list = []
        self.id_list.append(id)
        
    def setId(self, new_id):
        pass



class Department:
    def __init__(self, dept):
        self.dept =dept
        
        
    def findStudent(self, search_id):
        pass
    
    
    def addStudent(self, *args):
        pass
    
    
    def details(self):
        pass




s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()

