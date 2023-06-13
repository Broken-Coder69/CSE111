# 3. Write a python program that prints a list which contains cross multiplication between
# two given lists.

first = input()
second = input()


f_list = []
s_list = []

for i in first:
    if i != " ":
        f_list.append(i)
print(f_list)
for i in second:
    if i != " ":
        s_list.append(i)
print(s_list)

result = []
for i in f_list:
    for j in s_list:
        mul = int(i) * int(j)
        result.append(mul)
        
print(result)