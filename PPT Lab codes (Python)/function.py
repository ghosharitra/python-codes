"""
Recursion Q2)
A function f is defined as follows 
F(n)= (1) +(2*3) + (4*5*6) ... n. 
Given an integer n the task is to 
print the F(n)th term.

Input:
The first line of input contains an integer T 
denoting the number of test cases. 
Then T test cases follow. Each test contains an integer n.

Output:
For each test case print the nth term of the sequence. .

Constraints:
1 <= T <= 10
1 <= N <= 10

Example:
Input:
2
5
7
Output:
365527
6006997207
Q2 for today

"""

def sol(n,val=0):
    #print("n:",n,"val:",val)
    if n in d:
        return d[n]
    
    if n==0:
        return 0,1

    res,val=sol(n-1,val)

    s=1
    for i in range(n):
        s=s*val
        val+=1

    d[n]=(res+s,val)
    #print(">>>>n:",n,"val:",val)
    return res+s,val



d={}
for _ in range(int(input())):
    n=int(input())
    res,x=sol(n)
    print(res)