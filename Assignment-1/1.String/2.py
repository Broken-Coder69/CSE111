# 2. Given a string, print whether it is a number, word or mixed with digit andletters.
# If all the characters are numeric values, print NUMBER. If they are all letters, print WORD. If it is mixed, print MIXED.


given = "dasd"
word = 0
num = 0

for i in given:
    if "a" <= i <= "z":
        word += 1
        
    elif chr(48) <= i <= chr(57):
        num += 1
        

if word >0 and num == 0:
    print("Word")
elif word ==0 and num >0:
    print("Number")
elif word != 0 and num != 0:
    print("Mixed")        
    