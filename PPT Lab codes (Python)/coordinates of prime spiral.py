"""
The objective is to find the position (x and y coordinates) of a given prime.
Input Format:
The input consists of multiple lines.
The first line gives the number of primes (N) in this test case.
The next N lines contain one prime in each line.
Output Format:
The output consists of N lines.
Each consists of a space separated pair of integers giving the x and y coordinates of the corresponding prime in the input.
Constraints:
N≤10
Each prime < 1000000
Example 1
Input
2
3
7
Output
1 0
0 1
Explanation
There are 2 primes in this test case (N=2). The primes are 3 and 7. The coordinates of these in the spiral is (1,0) and (0,1).
The output hence has these in space separated form.
Example 2
Input
3
5
11
13
Output
1 1
1
1
1
0
Explanation
There are 3 primes in this test case (N=2). The primes are 5, 11 and 13. The coordinates of these in the spiral is (1,1), (1,1)
and (1,0).
The output hence has these in space separated form.

"""


def isPrime(n):
    
    i=3
    rootn=n**(1/2)
    while i<rootn+1:
        if(n%i==0):
            return False
        i=i+2
    else:
        return True
    



def genPrime(np):
    if(np==2):
        np=np+1
    else:
        np=np+2
    #print("np=",np)
    while not isPrime(np):
        
        np=np+2
        #print("np=",np)



    return np



def sol(terminalPrime):
    p=2
    i=0
    j=0

    c=2
    r=0


    while True:
        for k in range(c):
            #print("p=",p,"i=",i,"j=",j)
            if(p==terminalPrime):
                return i,j
            p=genPrime(p)
            if k!=c-1: 
                j=j+1
            else:
                i=i+1
        c=c+1

        for k in range(r):
            #print("p=",p,"i=",i,"j=",j)
            if(p==terminalPrime):
                return i,j
            p=genPrime(p)
            i=i+1
        r=r+1

        for k in range(c):
            #print("p=",p,"i=",i,"j=",j)
            if(p==terminalPrime):
                return i,j
            p=genPrime(p)
            if k!=c-1: 
                j=j-1
            else:
                i=i-1
        c=c+1

        for k in range(r):
            #print("p=",p,"i=",i,"j=",j)
            if(p==terminalPrime):
                return i,j
            p=genPrime(p)
            i=i-1
        r=r+1




terminalPrime=[]
try:
    t=int(input())
    for i in range(t):
        val=int(input())
        if(not isPrime(val)):
            raise Exception
        terminalPrime.append(val)

except:
    print(-1)
    exit(0)

for i in range(t):
    x,y=sol(terminalPrime[i])
    print(x,y)

