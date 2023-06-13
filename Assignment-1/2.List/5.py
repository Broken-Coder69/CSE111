# 5. BRACU has n students who are regular competitive programmers. According to the ACM ICPC rules, each person can participate in the
# regional championship at most 5 times.
# The head of the BRACU ACM Chapter is recently gathering teams to participate in this championship. 
# Each team must consist of exactly three people, at that, any person cannot be a member of two or more teams. What maximum number of teams
# can the head make if he wants each team to participate in the world championship  with the same members at least k times?
# The first line of input contains two integers, n and k. The next line contains n
# integers: y1,y2, ...,yn (0≤ yi≤ 5), where yi shows the number of times the i-thperson
# participated in the ACM ICPC Regional.
# Write a python program that prints how many teams can be formed according to
# the above problem statement.
# 5 2
# 0 4 5 1 0
# Sample Input 2
# 6 4
# 0 1 2 3 4 5
# Sample Input 3
# 6 5
# 0 0 0 0 0 0


n_k=input("Two integers:").split(" ")
talika=[]
n=int(n_k[0])
# print("Value of X -", x )


k=int(n_k[1])
# print("Value of Y -", y )


n_times=input("person participated in the ACM:").split(" ")
for i in n_times:
  value=int(i)+k
  if value<=5:
    talika.append(value)
temp=len(talika)
ans=temp//3
 
print(ans)