routine = ('CSE110-Mon/Wed-12:30','MAT110-Mon/Wed-2:00', 'ENG101-Sun/Tue-12:30', 'CSE110-Mon/Wed-9:30', 'PHY111-Sun/Tue-12:30')
routine_list = []
sub_list = []


time_list = []
course_status = ""


for i in routine:
    routine_list.append(i)
print("Routine :", routine_list)
    

    

for i in range(len(routine_list)):
    sub = routine_list[i][0:6]
    if sub not in sub_list:
        sub_list.append(sub)
    else:
        course_status += "You already have CSE110 in your routine"
      
       
    time = routine_list[i][7:-1]
    time_list.append(time)
    time_list[i] += "0"
    

print("Course: ", sub_list)
print("Time: ", time_list)    
