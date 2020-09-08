"""
Prime Counters

Problem : 
Given a number N, let CP(N) denote the number of primes between 1 and N (inclusive of N). We call N a prime counter if CP(N) is a prime (N need not be a prime).  For example, CP(3) = 2, CP(4) = 2, CP(5) = 2, CP(7) = 4.
Input Format:  
An integer T, number of test cases  T lines each containing two positive integers L, R separated by space
Output Format:  
T lines containing the number of prime counters between L and R (both inclusive) in the ith test case (or NONE is no prime counter exists in that range)
Constraints:  
L ≤ R ≤ 106

Example 1 

 Input  1
  1 10

Output 
 4

Explanation 
CP(1) = 0, CP(2) = 1, CP(3) = 2, CP(4) = 2, CP(5) = 3, CP(6) = 3, CP(7) = 4= CP(8) = CP(9) = CP(10)   Hence there are 4 prime counters, 3, 4, 5, 6 in the range 1 to 10.

Example 2  

Input  2
 2 20  3 30 

Output  
8
8

Explanation  
Upto 10, we have 4 prime counters. Between 11 and 20 the prime counters are 11, 12, 17, 18 and hence the count is 8. Between 21 and 30, we have no prime counters.

"""

def isPrime(n):
    if(n<2):
        return False
    elif(n==2):
        return True
    elif(n%2==0):
        return False
    else:
        for i in range(3,int(n**(1/2))+1,2 ):
            if(n%i==0):
                return False
        else:
            return True

def primeList(n):
    prime=[2]
    for i in range(3,n+1,2):
        if(isPrime(i)):
            prime.append(i)
    return prime

def sol(ll,ul):

    
    plist=primeList(ul)
    cp=[0]*(ul+1)
    for i in plist:
        cp[i]=1
    
    for i in range(ul):
        cp[i+1]=cp[i+1]+cp[i]


    res=0
    for i in range(ll,ul+1):
        if(isPrime(cp[i])):
            res+=1
    
    return res
            

ip=[]
try:
    t=int(input())

    for i in range(t):
        l=input().split()
        if(len(l)!=2):
            raise Exception
        ip.append(list(map(int,l)))
except:
    print("Invalid Input")
    exit(0)

for i in range(t):
    res=sol(ip[i][0],ip[i][1])
    print(res)