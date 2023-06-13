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