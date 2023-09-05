class Employee:
    
    total_employe = 0
    programmer_count = 0
    hr_count = 0
    intern_count_main = 0
    employee_count = {}
    count_list = []    
    
    given = ["HR", "Programmer", "Intern"]
    
    
    
    
    
    
    def __init__(self, name , joining_date, work_experience, weekly_work_hour=40) :
        self.name = name
        self.joining_date = joining_date
        self.work_experience = work_experience
        self.weekly_work_hour  = weekly_work_hour
        
        
        Employee.count_list = [Employee.hr_count, Employee.programmer_count, Employee.intern_count_main]
        print(Employee.given)
        print(Employee.count_list)
        
        for i in range(len(Employee.given)):
            Employee.employee_count[Employee.given[i]] = Employee.count_list[i]
            Employee.total_employe += Employee.count_list[i]
        print(f"Total Employee/s: {Employee.employee_count}")
        
        for k, v in Employee.employee_count.items():
            print(f"Total {k} Employee/s: {v}")
        
        
        

        
    def showDetails(self):
       print(f"Company workforce:")
       print(f"Total Employee/s: {Employee.employee_count}")
       


class Programmer(Employee):
    
    designation_list = [ "Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Technical Lead" ]
    

    def __init__(self, name, joining_date, work_experience, weekly_work_hour=40):
        super().__init__(name, joining_date, work_experience, weekly_work_hour=40)
        
        
        Employee.programmer_count += 1
        Employee.total_employe += 1
        
        self.id = ""
        self.designation = ""
        self.salary = ""
        year, month, date = self.joining_date.split("-")
        self.year = year
        self.month = month
        self.date = date
        self.initital = "P"
        self.weekly_work_hour = weekly_work_hour    
        
        self.salary_int = 0
        self.final_salary = 0

        
        
        if self.work_experience >= 0 and self.work_experience <3:
            self.designation += "Junior Software Engineer"        
        elif self.work_experience >= 3 and self.work_experience <5:
            self.designation += "Software Engineer"          
        elif self.work_experience >= 5 and self.work_experience <8:
            self.designation += "Senior Software Engineer"          
        elif self.work_experience >= 8:
            self.designation += "Technical Lead"
            

    def calculateSalary(self):
        if  self.designation == "Junior Software Engineer":
            self.salary += "BDT 30,000"
            self.salary_int = 30000
            self.final_salary = self.salary_int * (1.15 **(2023-int(self.year)))
            
            
            
            
        elif self.designation == "Software Engineer":
            self.salary += "BDT 45,000"
            self.salary_int = 45000
            self.final_salary = self.salary_int * (1.15 **(2023-int(self.year)))
            
                
            
        elif self.designation == "Senior Software Engineer":
            self.salary += "BDT 70,000"
            self.salary_int = 70000
            self.final_salary = self.salary_int * (1.15 **(2023-int(self.year)))
            
            
            
        elif self.designation == "Technical Lead":
            self.salary += "BDT 120,000"
            self.salary_int = 120000
            self.final_salary = self.salary_int * (1.15 **(2023-int(self.year)))
        # print(self.salary)
        
        
    def createProgrammerID(self):
        self.id = self.initital + "-" + self.year[2:] + self.month + self.date + "-" + str(Employee.total_employe)
        
        
    def calculateOvertime(self):
        if self.weekly_work_hour <= 40:
            print(self.name, "will not get overtime.")
        elif self.weekly_work_hour > 40:
            over_time_pay = 4 * (self.weekly_work_hour - 40) * 500
            self.final_salary += over_time_pay
            print(self.name, "will get BDT", over_time_pay, "overtime.")

        
    def showProgrammerDetails(self):
        self.calculateSalary()
        self.createProgrammerID()
        self.calculateOvertime()
        print("Programmer Employee:")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Joining Date: {self.joining_date}")
        print(f"Designation: {self.designation}")
        print(f"Salary: BDT {self.final_salary:.2f}")
        
        
        
        print(Employee.total_employe)
        print(Employee.programmer_count)
        


class HR(Employee):
    
    def __init__(self, name, joining_date, work_experience, weekly_work_hour=40):
        super().__init__(name, joining_date, work_experience, weekly_work_hour)
           
        
        year, month, date = self.joining_date.split("-")
        self.year = year
        self.month = month
        self.date = date
        self.initital = "HR"
        self.id = ""
        Employee.total_employe += 1
        Employee.hr_count += 0
        
        
        print(Employee.total_employe)
        

    def showHREmployeeDetails(self):
        self.createHREmployeeID()
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Joining Date: {self.joining_date}")
        
    def createHREmployeeID(self):
        Programmer.createProgrammerID(self)


class InternProgrammer(Programmer):
    intern_count = 0
    
    def __init__(self, name, joining_date, intern_type="Unpaid", work_experience=0, weekly_work_hour=40):
        super().__init__(name, joining_date, work_experience, weekly_work_hour)

        self.intern_type = intern_type
        self.temp_id = "Temp_"
        self.id = ""
        self.status = ""
        year, month, date = self.joining_date.split("-")
        self.year = year
        self.month = month
        self.date = date
        InternProgrammer.intern_count += 1
        Employee.intern_count_main = InternProgrammer.intern_count


    def showInternDetails(self):
        self.promoteToProgrammer()
        self.createInternEmployeeID()
        
        print(f"Intern (Programmer):")
        print(f"Name: {self.name}")
        
        
        
        if self.status == "Not Eligible for promotion":
            print(f"ID: {self.temp_id}")
        
        
        
        print(f"Joining Date: {self.joining_date}")
        print(f"Status: {self.status}")
        

    def promoteToProgrammer(self):
        if (8-int(self.month))<= 4:
            self.status += "Not Eligible for promotion"
            print(f"{self.name} is Not Eligible for promotion")
        else:
            self.status += "Eligible for promotion"
            print(f"{self.name} is Eligible for promotion")


    def createInternEmployeeID(self):
        if self.status == "Eligible for promotion":
            Programmer.createProgrammerID(self)
        elif self.status == "Not Eligible for promotion":
            self.temp_id += str(InternProgrammer.intern_count)
            






new = Employee("Richard Hendricks", "2021-06-08", 4, 48)
new.showDetails()
print("############## 1 ################")

richard = Programmer("Richard Hendricks", "2021-06-08", 4, 48)
richard.showProgrammerDetails()

print("############## 2 ################")

richard.calculateSalary()

print("############## 3 ##############")
richard.createProgrammerID()
print("############## 4 #############")
richard.calculateOvertime()
print("############## 5 ###############")
richard.showProgrammerDetails()


print("############## 6 ################")
# sda = Programmer("sdf", "2021-06-08", 4, 32)
# sda.calculateOvertime()
monica = HR("Monica Hall", "2022-07-06", 2, 40)
print("############## 7 ################")
monica.showHREmployeeDetails()
print("############## 8 ###############")
monica.createHREmployeeID()

print("############## 9 #################")
jared = InternProgrammer("Jared Dunn", "2023-06-05", "Paid")
jared.showInternDetails()
print("############## 10 #################")
jared.promoteToProgrammer()


print("###### 3453 ############")
yang = InternProgrammer("Jian Yang", "2023-01-01")
yang.showInternDetails()
yang = yang.promoteToProgrammer()







