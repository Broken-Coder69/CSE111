#task 5
class Department:
  def __init__(self,dept="ChE Department",sec=5):
    self.dept=dept
    self.sec=sec
    self.avg=0
    print(f"The {self.dept} has {self.sec} sections.")
  def add_students(self,*students):
    if self.sec==len(students):
      sum=0
      for i in students:
        sum+=i
      self.avg=sum/len(students)
      print(f"The {self.dept} has an average of {self.avg} students in each section.")
    else:
      print(f"{self.dept} doesn't have {len(students)} sections.")

  def merge_Department(self,*ob): 
    merge_avg=self.avg*self.sec
    for i in ob:
      print(f"{i.dept} is merged to {self.dept}")
      merge_avg+=i.avg*i.sec
    print(f"Now the {self.dept} has an average of {merge_avg} students in each section.")


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