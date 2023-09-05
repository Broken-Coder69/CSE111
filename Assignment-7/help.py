class Employee:
    total_employees = 0
    total_programmer_employees = 0
    total_hr_employees = 0
    ent = 0
    
    def _init_(self, name, joining_date):
        self.name = name
        l = []
        x = joining_date.split("-")
        for i in x:
            l.append(i)
        p = str(l[2]) + "-" + str(l[1]) + "-" + str(l[0])
        self.joining_date = p
        Employee.total_employees += 1
    
    @classmethod
    def showDetails(cls):
        print("Company workforce:")
        print("Total Employee/s:", cls.total_employees)
        if cls.total_programmer_employees != 0:
            print("Total Programmer Employee/s:", cls.total_programmer_employees)
        if cls.total_hr_employees != 0:
            print("Total HR Employee/s:", cls.total_hr_employees)


class Programmer(Employee):
    def _init_(self, name, joining_date, years_of_experience, weekly_work_hours = 40):
        super()._init_(name, joining_date)
        self.years_of_experience = years_of_experience
        self.weekly_work_hours = weekly_work_hours
        self.pos = None
        self.sal = 0
        if self.weekly_work_hours < 40:
            print(self.name, "can not work for", self.weekly_work_hours, "hours")
        Employee.total_programmer_employees += 1
            
            

    def calculateSalary(self):
        if 0 <= self.years_of_experience < 3:
            self.pos = "Junior Software Engineer"
            self.sal = 30000
            for i in range(23 - int(self.joining_date[8] + self.joining_date[9])):
                self.sal += (self.sal * (15/100)) 
        elif 3 <= self.years_of_experience < 5:
            self.pos = "Software Engineer"
            self.sal = 45000
            for i in range(23 - int(self.joining_date[8] + self.joining_date[9])):
                self.sal += (self.sal * (15/100))
        elif 5 <= self.years_of_experience < 8:
            self.pos = "Senior Software Engineer"
            self.sal = 70000
            for i in range(23 - int(self.joining_date[8] + self.joining_date[9])):
                self.sal += (self.sal * (15/100))
        elif 8 <= self.years_of_experience:
            self.pos = "Technical Lead"
            self.sal = 120000
            for i in range(23 - int(self.joining_date[8] + self.joining_date[9])):
                self.sal += (self.sal * (15/100))

    def calculateOvertime(self):
        if self.weekly_work_hours <= 40:
            print(self.name, "will not get overtime.")
        elif self.weekly_work_hours > 40:
            over_time_pay = 4 * (self.weekly_work_hours - 40) * 500
            self.sal += over_time_pay
            print(self.name, "will get BDT", over_time_pay, "overtime.")
    def showProgrammerDetails(self):
        print("Programmer Employee:")
        print("Name:", self.name)
        print("ID:", "P-" + self.joining_date[8] + self.joining_date[9] +  self.joining_date[3] + self.joining_date[4] + self.joining_date[0] + self.joining_date[1] +"-" + str(Employee.total_employees))
        print("Joining Date:", self.joining_date)
        print("Designation:",self.pos)
        print("Salary: BDT", self.sal)


        
class HR(Employee):
    def _init_(self, name, joining_date, years_of_experience, weekly_work_hours=40):
        super()._init_(name, joining_date)
        self.years_of_experience = years_of_experience
        self.weekly_work_hours = weekly_work_hours
        if self.weekly_work_hours < 40:
            print(self.name, "can not work for", self.weekly_work_hours, "hours")
        Employee.total_hr_employees += 1
    
    def showHREmployeeDeatails(self):
        print("HR Employee:")
        print("Name:", self.name)
        print("ID:", "P-" + self.joining_date[8] + self.joining_date[9] +  self.joining_date[3] + self.joining_date[4] + self.joining_date[0] + self.joining_date[1] +"-" + str(Employee.total_employees))
        print(f"Joining Date: {self.joining_date}")


class InternProgrammer(Employee):
    def _init_(self, name, joining_date, intern_type="Unpaid"):
        self.name = name
        self.joining_date = joining_date
        self.intern_type = intern_type
        Employee.ent += 1
    
    def showInternDetails(self):
        print("Intern (Programmer):")
        print("Name:", self.name)
        print("ID:", "Temp" +"-" + str(Employee.ent))
        print("Joining Date:", self.joining_date)
        print("Type:", self.intern_type)
        if (8 - int(self.joining_date[5] + self.joining_date[6])) > 4:
            print(self.name, "is promoted.")
        else:
            print(self.name, "is not promoted.")
        
    def promoteToProgrammer(self):
        if (8 - int(self.joining_date[5] + self.joining_date[6])) > 4:
            print(self.name, "is promoted.")
            return Programmer(self.name, self.joining_date, 0, 40)
        else:
            print(self.name, "is not promoted.")
        




Employee.showDetails()
print("=========1=========")
richard = Programmer("Richard Hendricks", "2021-06-08", 4, 48)
richard.calculateSalary()
print("=========2=========")
richard.showProgrammerDetails()
print("=========3=========")
richard.calculateOvertime()
print("=========4=========")
richard.showProgrammerDetails()
print("=========5=========")
monica = HR("Monica Hall", "2022-07-06", 2, 40)
print("=========6=========")
monica.showHREmployeeDeatails()
print("=========7=========")
Employee.showDetails()
print("=========8=========")
gilfoyle = Programmer("Bertram Gilfoyle", "2020-03-02", 6, 35)
gilfoyle.calculateSalary()
print("=========9=========")
gilfoyle.calculateOvertime()
print("=========10=========")
gilfoyle.showProgrammerDetails()
print("=========11=========")
gavin = Programmer("Gavin Belson", "2016-12-20", 9)
gavin.calculateSalary()
gavin.calculateOvertime()
gavin.showProgrammerDetails()
print("=========12=========")
yang = InternProgrammer("Jian Yang", "2023-01-01")
yang.showInternDetails()
print("=========13=========")
jared = InternProgrammer("Jared Dunn", "2023-06-05", "Paid")
jared.showInternDetails()
print("=========14=========")
jared = jared.promoteToProgrammer()
print("=========15=========")
Employee.showDetails()
print("=========16=========")
yang = yang.promoteToProgrammer()
yang.calculateSalary()
yang.showProgrammerDetails()
print("=========17=========")
Employee.showDetails()