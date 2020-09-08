"""
In a crossover fantasy universe, Houin Kyoma is up in a battle against a very powerful monster Nomu that can kill Houin Kyomain a single blow. 
However being a brilliant scientist Houin  Kyoma found a way to pause time for exactly M sec. Every sec,Houin  Kyoma attacks monster  Nomu with certain power, which will reduce monster Nomus's health points by that exact power. Initially Nomu has H Health Points. Nomu dies when his Health Points reach to ZERO . Normally Houin  Kyoma performs Normal Attack with power A. Besides from Kyoma’s brilliance, luck plays a major role in events of this crossover fantasy universe. Houin  Kyoma’s Luck L is refereed as probability of performing a super attack. 
A super attack by Houin Kyoma increases power of Normal Attack by value C. Given this information calculate &  print the probability that Houin  Kyoma kills monster Nomu & survives. If Houin  Kyoma dies print “RIP”. 
 Constraints
0 < T <= 50
1 <= A, H, C, L1, L2 <= 1000
1 <= M <= 20.
L1<=L2 
Input Format
First line :  T no. of test cases.
Each test case :  single line with space separated numbers A H L1 L2 M C. 
Where luck L is refer  as L1/L2 else numbers are  as described above.
Output 
Print probability that Houin Kyoma kills monster Nomu in form P1/P2 where P1<=P2 & gcd(P1,P2)=1. Print “RIP” If impossible .
Explanation 
Input
2
10 33 7 10 3 2
10 999 7 10 3 2
Output
98/125

"""
import math

def fadd(a,b,c,d):
    res1=0
    res2=0

    if b==d:
        res1=a+c
        res2=b 
        return res1,res2

    








def fsub(a,b,c,d):
    pass


def fmul(a,b,c,d):
    pass









def sol(t,info):
    res=[]
    for i in range(t):
        a,h,l1,l2,m,c=info[i][0],info[i][1],info[i][2],info[i][3],info[i][4],info[i][5]
        if h- m*(a+c)>0:
            s="RIP"
            res.append(s)
            continue
        
        rhp=h- a*m
        if rhp<= 0:
            s="1/1"
            res.append(s)
            continue
        
        r=math.ceil(rhp/c)
        n=m

        ps=l1/l2
        pns=(l2-l1)/l2
        
        

        prob=0
        for i in range(r,m+1):
            val=math.perm(n,r)*((ps)**i)*((pns)**(m-i))
            prob=prob+val
            print("val:",val)
        print("prob:",prob)
        s=prob
        res.append(s)


    return res

try:
    t=int(input())
    info=[]
    for i in range(t):
        temp=list(map(int,input().split() ))
        if len(temp)!=6:
            raise Exception
        info.append(temp)
except:
    print("Invalid Input")
    exit(0)

res=sol(t,info)
for i in range(t):
    print(res[i])