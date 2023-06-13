# 4. Create a string from two given strings by concatenating common characters of the given strings.

here = "dean, tom"

ager = ""
porer = ""

for i in here:
    if i == ",":
        break
    else:
        ager += str(i)
        
porer += here[len(ager)+2 : len(here)]

final = ""
for i in ager:
    if i in porer:
        final += str(i)

    
for i in porer:
    if i in ager:
        final += str(i)


if len(final) != 0:
    print(final)
else:
    print("Nothing in common")