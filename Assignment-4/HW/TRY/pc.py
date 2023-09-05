routine = ('CSE110-Mon/Wed-12:30','MAT110-Mon/Wed-2:00', 'ENG101-Sun/Tue-12:30', 'CSE110-Mon/Wed-9:30', 'PHY111-Sun/Tue-12:30')
routine_list = []
sub_list = []
day_list = []
time_list = []
course_status = ""


for i in routine:
    routine_list.append(i)
print(routine_list)
    

    

for i in range(len(routine_list)):
    sub = routine_list[i][0:6]
    if sub not in sub_list:
        sub_list.append(sub)
    else:
        course_status += "You already have CSE110 in your routine"
        
        
    day = routine_list[i][7:14]
    day_list.append(day)
    
    
    
    time = routine_list[i][15:-1]
    time_list.append(time)
    time_list[i] += "0"
    
    
for i in range(len(day_list)):
    if day_list[i] == time_list[i]:
        print("cant")



print("Course: ", sub_list)
print("Date ", day_list)
print("Time: ", time_list)    




# print(routine_list[0][0:6])
# print(routine_list[1][0:6])

# for i in range(len(routine_list)):
#     sub = routine_list[i][0:6]
#     sub_list.append(sub)
    
#     day = routine_list[i][7:14]
#     day_list.append(day)
    
#     time = routine_list[i][15:-1]
#     time_list.append(time)
#     time_list[i] += "0"




# Successfully added CSE110!
# Successfully added MAT110!
# Successfully added ENG101!
# You already have CSE110 in your
# routine
# Can't take PHY111. It's clashing with
# your ENG101
# -----------------

# st1.addCourses('CSE110-Mon/Wed-12:30',
# 'MAT110-Mon/Wed-2:00')
# st1.addCourses('ENG101-Sun/Tue-12:30',
# 'CSE110-Mon/Wed-9:30')
# st1.addCourses('PHY111-Sun/Tue-12:30')


