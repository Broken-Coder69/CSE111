
# 4
# 1 2 3
# 4 5 6
# 10 11 12
# 7 8 9


num = int(input())
highest_sum = 0
highest_list = []

for i in range(0, num):
    given = input().split()
    given_list = []
    given_sum = 0
    
    for i in given:
        given_list.append(int(i))
        
    for i in given:
        given_sum += int(i)
        
        
    if highest_sum <= given_sum:
        highest_sum = given_sum
        highest_list = given_list
        

        
print(highest_sum)
print(highest_list)












# num=int(input("Enter the list number: "))
# max_sum=0
# max_list=[]

# for i in range (0,num):
#   sum=0
#   var=input("value of the list:")
#   x=var.split(" ")
#   z=[]
  
#   for k in x:
#     z.append(int(k))
  
#   for j in x:
#     sum= sum+int(j)
  
#   if max_sum<sum:
#     max_sum=sum
#     max_list=z

# print(max_sum)
# print(max_list)