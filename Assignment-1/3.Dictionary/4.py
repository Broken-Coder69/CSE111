#5.

# given= "Hello, World!"

# for i in range (0,len(given)):
#    words =ord(given[i])
#    if words>=97 and words<=122:
#        words=words-32
#    big =chr(words)
#    print(big,end="")

# keys = ""
# key_list = {1 :".,?!:"
#            ,2 :"ABC"
#            ,3: "DEF"
#            ,4 :"GHI"
#            ,5 :"JKL" 
#            ,6 :"MNO"
#            ,7: "PQRS"
#            ,8 :"TUV"
#            ,9 :"WXYZ"
#            ,0 :" "}

# for i in given:
#     for key,values in key_list.items():
#         if i in values:
#             button_press = values.index(i)+1
#             key += str(key)*button_press
            
# print(key)

# for letter in given:
#   for key,values in key_list.items():
#     if letter in values:
#       press=values.index(letter)+1
#       keys=keys+str(key)*press

# print(keys)


var=input()
for i in range (0,len(var)):
   words =ord(var[i])
   if words>=97 and words<=122:
       words=words-32
   big =chr(words)
   print(big,end="")
   
print(var)

# output=""
# dict1={1 :".,?!:",2 :"ABC",3: "DEF",4 :"GHI", 5 :"JKL" 
#           ,6 :"MNO"
#             ,7: "PQRS"
#             ,8 :"TUV"
#             ,9 :"WXYZ"
#             ,0 :" "}

# for letter in var:
#   for key,values in dict1.items():
#     if letter in values:
#       press=values.index(letter)+1
#       output=output+str(key)*press

# print(output)

# Hello, World!










# var=input().upper()
# output=""
# dict1={1 :".,?!:",2 :"ABC",3: "DEF",4 :"GHI", 5 :"JKL" 
#           ,6 :"MNO"
#             ,7: "PQRS"
#             ,8 :"TUV"
#             ,9 :"WXYZ"
#             ,0 :" "}

# for letter in var:
#   for key,values in dict1.items():
#     if letter in values:
#       press=values.index(letter)+1
#       output=output+str(key)*press

# print(output)