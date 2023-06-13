# 1. Write a Python program to combine two dictionaries into one by adding values for
# common keys. Input contains two comma separated dictionaries. Print the new
# dictionary and create a tuple which contains unique values in sorted order.
# a: 100, b: 100, c: 200, d: 300
# a: 300, b: 200, d: 400, e: 200


first_dict = input().split(", ")
second_dict = input().split(", ")
main_dict ={}




for i in first_dict:
  i = i.split(": ")
  main_dict[i[0]] = int(i[1])



for i in second_dict:
  i = i.split(": ")
  if i[0] not in main_dict.keys():
    main_dict[i[0]] = int(i[1])
  else:
    main_dict[i[0]]+= int(i[1])
    
print(main_dict)


value = []

for i in main_dict.values():
    value.append(i)

value = []
for i in main_dict.values():
    if i not in value:
        value.append(i)


val = tuple(value)
val = sorted(val)
print("Values: ",tuple(val))