# 3. Write python code to invert a dictionary. It should print a dictionary where the keys
# are values from the input dictionary and the values are lists of keys from the input
# dictionary having the same value. Make sure the program handles multiple same values.
# Sample Input
# key1 : value1, key2 : value2, key3 : value1
# Sample Output
# { "value1" : ["key1", "key3"], "value2" : ["key2"] }

# ls = input().split(", ")
# print(ls)


# given = ['key1 : value1', 'key2 : value2', 'key3 : value1']
# dic = {}
# for i in given:
#     dic.update({})


main_dict = {}
given=input().split(",")
for i in given:
  order=i.split(":")
  
  if order[1] not in main_dict:
    main_list=[]
    main_list.append(order[0])
    main_dict[order[1]]=main_list
  else:
    main_list=[]
    main_list.append(order[0])
    main_dict[order[1]]=main_dict[order[1]]+main_list
print(main_dict)

# key1 : value1, key2 : value2, key3 : value1