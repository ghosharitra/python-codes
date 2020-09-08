"""
You are given a strictly convex polygon with N vertices (numbered 1 through N). For each valid i, the coordinates of the i-th vertex are (Xi,Yi). You may perform the following operation any number of times (including zero):

Consider a parent polygon. Initially, this is the polygon you are given.
Draw one of its child polygons ― a simple non-degenerate polygon such that each of its sides is a chord of the parent polygon (it cannot be a side of the parent polygon). The operation cannot be performed if the parent polygon does not have any child polygons.
The child polygon which you drew becomes the new parent polygon.
Your goal is to draw as many sides of polygons in total as possible (including the polygon given at the start). Find this maximum total number of sides.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
N lines follow. For each valid i, the i-th of these lines contains two space-separated integers Xi and Yi.
Output
Print a single line containing one integer ― the maximum possible number of sides of polygons.

Constraints
1≤T≤1,000
3≤N≤105
|Xi|,|Yi|≤109 for each valid i
the sum of N over all test cases does not exceed 2⋅106
Example Input
2
4
-100 1
0 2
0 0
100 1
7
-4 0
-3 -2
-3 2
0 -4
2 -3
2 3
3 2
Example Output
4
10


All submissions for this problem are available.
Author:	5★pandey__ji
Editorial:	https://discuss.codechef.com/problems/POLYREL
Tags:	cook121, easy, geometry, greedy, pandey__ji, pandey__ji, psychik
Date Added:	15-08-2020
Time Limit:	1.5 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ
"""

d={}

def sol(n):
    if(n in d):
        return d[n]
    if n<3:
        return 0
    
    res=n
    res+=sol(n//2)
    d[n]=res
    return res

t=int(input())
for _ in range(t):
    
    n=int(input())
    for _ in range(n):
        input()
    
    
    print(sol(n))
    print(d)