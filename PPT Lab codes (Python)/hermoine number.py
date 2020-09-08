"""
10
77883 48760 68269 31574 57351 20528 45398 54148 37399 31382
10
5 9
2 8
2 9
6 6
1 3
1 9
7 8
6 10
2 7
1 2
"""

#from math import factorial


MOD=1000000007


def factorial(x):
  p=1
  for i in range(1,x+1):
    p=(p*i)%MOD
  return p



n=int(input())

h=[]

arr=list(map(int,input().split()))
fact=list(map(lambda i: factorial(i)%MOD,arr))



n1=int(input())
for j in range(n1): 
  a=list(map(int,input().split()))
  l=a[0]
  r=a[1]

  prod=1
  for i in range(l-1,r):
    #print(math.factorial(arr[i]))
    prod=(prod*fact[i])%MOD

  h.append(((prod)**(r-l))%MOD)
  print("hermoine number: ", h[j]) 

print("hermoine number: ",h) 














