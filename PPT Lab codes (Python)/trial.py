"""
Chef opted for Bio-Statistics as an Open-Elective course in his university, but soon got bored, and decided to text his friends during lectures. The instructor caught Chef, and decided to punish him, by giving him a special assignment.

There are N numbers in a list A=A1,A2,…,AN. Chef needs to find the mode of the frequencies of the numbers. If there are multiple modal values, report the smallest one. In other words, find the frequency of all the numbers, and then find the frequency which has the highest frequency. If multiple such frequencies exist, report the smallest (non-zero) one.

More formally, for every v such that there exists at least one i such that Ai=v, find the number of j such that Aj=v, and call that the frequency of v, denoted by freq(v). Then find the value w such that freq(v)=w for the most number of vs considered in the previous step. If there are multiple values w which satisfy this, output the smallest among them.

As you are one of Chef's friends, help him complete the assignment.

Input:
The first line contains an integer T, the number of test cases.
The first line of each test case contains an integer N, the number of values in Chef's assignment.
The second line of each test case contains N space-separated integers, Ai, denoting the values in Chef's assignment.
Output:
For each test case, print the mode of the frequencies of the numbers, in a new line.

Constraints
1≤T≤100
1≤N≤10000
1≤Ai≤10
Subtasks
30 points : 1≤N≤100
70 points : Original constraints.
Sample Input:
2
8
5 9 2 9 7 2 5 3
9
5 9 2 9 7 2 5 3 1
Sample Output:
2
1
Explanation:
Test case 1: (2, 9 and 5) have frequency 2, while (3 and 7) have frequency 1. Three numbers have frequency 2, while 2 numbers have frequency 1. Thus, the mode of the frequencies is 2.

Test case 2: (2, 9 and 5) have frequency 2, while (3, 1 and 7) have frequency 1. Three numbers have frequency 2, and 3 numbers have frequency 1. Since there are two modal values 1 and 2, we report the smaller one: 1.

Author:	akash_adm
Date Added:	29-08-2020
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ
Submit

"""


from collections import *
n=[]
num=[]
l1=[]
res=[]
res1=[]
result=[]

t=int(input())
for i in range(t):
    temp=int(input())
    n.append(temp)
    temp2=list(map(int,input().split()))
    num.append(temp2)
    
    
#print(num)
for i in range(t):
    f=Counter(num[i])
    #print(f)

    

    for j,k in f.items():
        l1.append(k)

    print("l1:",l1)
    res=Counter(l1)

    print("res:",res)
    for j,k in res.items():
        res1.append(k)

    #print(res1)
    m=max(res1)
    for j,k in res.items():
        if k==m:
            result.append(j)
    print(result)        
    minimum=min(result)
    print(minimum)