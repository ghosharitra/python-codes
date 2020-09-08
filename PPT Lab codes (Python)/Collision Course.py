"""

5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2



"""


import math 
def eulers(x,y):
   return math.sqrt(x*x + y*y) 


def combination(n):
    return math.factorial(n)/(math.factorial(2)*math.factorial(n-2))


t=int(input())
info=[]
for i in range(t):
    temp=list(map(int,input().split()))
    info.append(temp)
print(info)

time=[]
for i in range(t):
    time.append(eulers(info[i][0],info[i][1])/info[i][2])

print(time)

utime=list(set(time))
print(utime)

sum=0
for i in utime:
    count=0
    for j in time:
        if i==j:
            count=count+1
    
    sum=sum+combination(count)

print(int(sum))
