talika = []
for i in range(30):
    num = input("Enter: ")
    if num != "STOP":
        talika.append(int(num))
    else:
        break



count = {}
for i in talika:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
print(count)

for k,v in count.items():
    print(k, "-", v, "times")




# a = "STOP"
# lst=[]
# while a!=0:
#   n= input()
#   lst.append(n)
#   if n==a:
#     break
# lst1=lst[:-1]
# lst2=[]
# count=0
# for i in lst1:
#   if i not in lst2:
#     lst2.append(i)
#     for j in range(len(lst1)):
#       if i == lst1[j]:
#         count+=1
#     print(i,"-",lst1.count(i), "times")    