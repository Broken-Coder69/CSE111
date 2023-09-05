class StudentRoutineGenerator:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        
        
        print(f"Name: {self.name}")
        print(f"Maximum Number of Courses: {self.course}")
        print("Initial Routine: {'Sat/Thurs': {}, 'Sun/Tue': {}, 'Mon/Wed': {}}")
        
        
        self.routine_list = []
        self.sub_list = [] 
        self.time_list = []
        self.course_status = ""
        
    def addCourses(self, *routines):
        if routines:
            for i in routines:
                self.routine_list.append(i)
            print(self.routine_list)
            
            for i in range(len(self.routine_list)):
                sub = self.routine_list[i][0:6]
                # if sub not in self.sub_list:
                self.sub_list.append(sub)
                # print(f"Successfully added {sub}!")
                
                
                    

                    
                    

                
                time = self.routine_list[i][7:-1]
                self.time_list.append(time)
                self.time_list[i] += "0"
        
                

                
 
                
    
    
    def showRoutine(self):
        pass
    
    
    
    def dropCourse(self, sub):
        pass 
        









print('##################################')
st1 = StudentRoutineGenerator('Harry', 4)
print('------------------------------')
st1.addCourses('CSE110-Mon/Wed-12:30','MAT110-Mon/Wed-2:00')
st1.addCourses('ENG101-Sun/Tue-12:30','CSE110-Mon/Wed-9:30')
st1.addCourses('PHY111-Sun/Tue-12:30')
print('------------------------------')
st1.showRoutine()
print('------------------------------')
st1.dropCourse('CSE110')
st1.dropCourse('PHY112')
print('------------------------------')
st1.showRoutine()
print('##################################')
st2 = StudentRoutineGenerator('John', 3)
print('------------------------------')
st2.addCourses('MAT110-Mon/Wed-8:00')
st2.addCourses('ENG101-Sat/Thurs-12:30',
'CSE110-Sun/Tue-9:30')
st2.addCourses('PHY111-Sun/Tue-12:30')
print('------------------------------')
st2.showRoutine()
