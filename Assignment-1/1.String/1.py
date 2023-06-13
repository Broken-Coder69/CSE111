# 1. From a given string, print the string in all uppercase if the number ofuppercase letters is more than lowercase letters.
# Otherwise, if lowercase is greater or equal to uppercase letters, print all lowercase. The inputs will contain letters (A-Z, a-z) only.

given = "BaNaNa"
updated = ""
upper = 0
lower = 0

for i in given:
    if chr(65) <= i <= chr(90):
        upper += 1
        
    elif chr(97) <= i <= chr(122):
        lower += 1

if upper>lower:
  for i in given:
    if 97 <= ord(i) <= 122:
      updated += chr(ord(i)- 32)
    else:
      updated += i

else:
  for i in given:
    if 65 <= ord(i) <= 90:
      updated += chr(ord(i) + 32)
    else:
      updated += i

print(updated)  