# 3. In a given string, there will be two uppercase letters in between some lowercase letters. 
# Print the substring from the first uppercase letter to the last uppercase letter excluding them. 
# If there are no letters in between them, print the word BLANK. It is guaranteed that there will be only two uppercase letters in the string.


here = "coDIng"
ager = ""
porer = ""

for i in here:
    if "a" <= i <= "z":
        ager += str(i)
    elif 'A' <= 'Z':
        break
    



final = here[int(len(ager)+1):-1]


for i in final:
    if "a" <= i <= "z":
        porer += str(i)
    elif 'A' <= 'Z':
        break
    
if len(porer) > 0:
    print(porer)

elif len(porer) == 0:
    print("BLANK")