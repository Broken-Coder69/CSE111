class Department:
    def __init__(self, dept="ChE", sec=5):
        self.dept = dept
        self.sec = sec
        self.sec_list = []
        self.avg_count = 0
        self.merged_list = []
        self.avg = 0
        
        
        print(f"The {self.dept} Department has {self.sec} sections.")
        
    def add_students(self, *sections):
        if len(sections) == self.sec:

            for i in sections:
                self.sec_list.extend(sections)
            for i in range(self.sec):
                self.avg_count += self.sec_list[i]
                avg = self.avg_count / self.sec
                dui_ghor = "%.2f" % avg
                self.avg = dui_ghor
            print(f"The {self.dept} Department has an average of {dui_ghor} students in each section.")
            
        else:
            print(f"The {self.dept} Department doesn't have {len(sections)} sections.")
            
        


    def merge_Department(self,*ob):
        merge_avg=self.avg*self.sec
        for i in ob:
            print(f"{i.dept} is merged to {self.dept}")
            merge_avg+=i.avg*i.sec
        print(f"Now the {self.dept} has an average of {merge_avg} students in each section.")
            

    # def merge_Department(self, department):
    #     merged_department = Department('Engineering Department', self.sections)
    #     merged_department.students.extend(self.students)
    #     merged_department.students.extend(department.students)
    #     merged_department.sections += department.sections
    #     return merged_department








d1 = Department()
print('1-----------------------------------')
d2 = Department('MME Department')
print('2-----------------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------------')
mega = Department('Engineering Department',
10)
print('7-----------------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------------')
print(mega.merge_Department(d3))


# The ChE Department has 5 sections.
# 1-----------------------------------
# The MME Department has 5 sections.
# 2-----------------------------------
# The NCE Department has 8 sections.
# 3-----------------------------------
# The ChE Department has an average of 20.4 students in
# each section.
# 4-----------------------------------
# The MME Department doesn't have 3 sections.
# 5-----------------------------------
# The NCE Department has an average of 29.88 students in
# each section.
# 6-----------------------------------
# The Engineering Department has 10 sections.
# 7-----------------------------------
# The Engineering Department has an average of 30.7
# students in each section.
# 8-----------------------------------
# ChE Department is merged to Engineering Department.
# MME Department is merged to Engineering Department.
# Now the Engineering Department has an average of 40.9
# students in each section.
# 9-----------------------------------
# NCE Department is merged to Engineering Department.
# Now the Engineering Department has an average of 64.8
# students in each section.