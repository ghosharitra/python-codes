"""
Chef is the leader of Chef's Earth Defense Organization, and his mission is to counter aliens which are threatening the earth. According to information gathered by the organization, there are N alien spaceships (numbered 1 through N) planning to invade the earth. The i-th spaceship will appear on the radar at time Ci. Each spaceship needs D time to reach earth once it appears on the radar.

Chef's organization owns a huge laser cannon which can destroy one spaceship in one shot. However, once the cannon is used once it needs some amount of cool-down time in order to be used again (first shot doesn't require cool-down time before it is used). This cool-down time, however, is configurable. It has to be set before the first shot, and cannot be changed after that. If Chef sets a lower cool-down time, that would increase the energy consumed by the cannon, and vice-versa - the higher the cool-down time, the lower the energy consumed.

This might be a long battle, and Chef wants to use as little energy as possible. So Chef wants to maximize the cool-down time while still being able to destroy all spaceships before any of them arrive on earth. In particular, the i-th spaceship should be shot between the times Ci and Ci+D (both end points inclusive).

Input:
The first line of input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two integers N and D.
The second line contains N space-separated integers C1,C2,…,CN.
Output:
For each test case, print a single line containing one real number― the maximum cool-down time possible. Your answer will be considered correct if the absolute or relative error of the answer does not exceed 10−6.

Constraints
1≤T≤1000
2≤N≤105
1≤Ci≤109 for each valid i
1≤D≤109
The sum of N over all test cases does not exceed 106
Subtasks
Subtask #1 (50 points):

N≤1,000
the sum of N over all test cases does not exceed 10,000
Subtask #2 (50 points): Original constraints

Sample Input:
2
3 2
3 2 3
2 1
5 6
Sample Output:
1.5000000000
2.0000000000
Author:	6★kingofnumbers
Date Added:	28-08-2020
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ
Submit
All Submissions
Successful Submissions


"""


for _ in range(int(input())):
    n,d=map(int,input().split())
    data=list(map(int,input().split()))

    min=999999
    max=-999999
    for i in data:
        if min>i:
            min=i

        if max<i+d:
            max=i+d
    print( '%.10f'%((max-min)/(n-1)) )
    


