# Let there are N numbers in a list and that list is said to be a UB Jumper if the absolute values of the difference between the 
# successive elements take on all thevalues 1 through N − 1. For example, 2 1 4 6 10 is a UB Jumper because the absolute
# differences between them are 1 3 2 4 which is all numbers from 1 to (5 - 1) or 4.
# Write a python program that takes a number sequence as input and prints
# whether it is a UB Jumper or Not UB Jumper. Input will stop after getting
# “STOP” as input. (Number order or absolute difference order doesn’t follow any
# sequence.)


# 1 4 2 3
# 2 1 4 6 10
# 1 4 2 -1 6
# STOP

while True:
    number = input().split()

    if "STOP" in number:
        break
    else:
        for i in range(len(number)):
            number[i] = int(number[i])

        check_list = []
        for i in range(len(number)-1):
            check_list.append(number[i] - number[i+1])
            check_list[i] = abs(check_list[i])
                  
            
        for j in range(1,len(number)):
            if j in check_list:
                result = "UB Jumoer"
            else:
                result = "Not UB Jumper"
        print(result)

