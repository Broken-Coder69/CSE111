#TASK 6
class StudentRoutineGenerator:
  def __init__(self,name,num):
    print(f"Name: {name}")
    print(f"Maximum Number of Courses: {num}")
    self.dic={'Sat/Thurs': {}, 'Sun/Tue': {}, 'Mon/Wed': {}}
    print(f"Initial Routine: {self.dic}")
    self.course_list=[]
    self.date_list=[]
    
  def addCourses(self,*course):
    dic={}
    c_name=""
    date=""
    time=""
    count=0
    num=0
    flag=False
    for i in course:
      for j in range(len(i)):
        if i[j]=="-":

          count+=1
          if count==1:
            c_name=i[:j:]
            if c_name in self.course_list:
              print(f"You already have {c_name} in your routine")
              flag=True

          if count==2:
            date=i[num+1:j]
            self.date_list0.append(date)
            num=j
            break
          num=j

      time=i[num+1:]
      if time in self.dic[date].keys():
        print(f"Can't take {c_name}. It's clashing with your {self.dic[date][time]} ")
        break
      if flag:
        continue
      else:
        print(f"Successfully added {c_name}! ")
        self.c_lis.append(c_name)
      self.dic[date][time]=c_name
      count=0
  def showRoutine(self):
    print(f"Updated Routine: {self.dic}")
    print("Routine Details:")
    for key,value in self.dic.items():
      if key in self.date_list:
        print(f"{key}:")
      for i,j in value.items():
        print(f"{i}-{j}")
  def dropCourse(self,name):
   for key,value in self.dic.items():
    for i,j in value.items():
      if j==name:
        del self.dic[key][i]


print('##################################')
st1 = StudentRoutineGenerator('Harry', 4)
print('------------------------------')
st1.addCourses('CSE110-Mon/Wed-12:30', 'MAT110-Mon/Wed-2:00')
st1.addCourses('ENG101-Sun/Tue-12:30', 'CSE110-Mon/Wed-9:30')
st1.addCourses('PHY111-Sun/Tue-12:30')
print('------------------------------')
st1.showRoutine()
print('------------------------------')
st1.dropCourse('CSE110')
st1.dropCourse('PHY112')