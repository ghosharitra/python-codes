"""
Chef's apartment consists of M floors (numbered 1 through M), and there's an elevator that is used to move between different floors. The elevator is connected with a computer which registers its movement in a sequence B. Whenever the elevator moves to a different floor, the computer appends the new floor number to sequence B. Currently, the sequence B has N elements.

Unfortunately, the computer is infected with a virus which replaced some elements of B by −1s. Chef now wants to know what could be the minimum number of times the elevator has changed its direction. That is, how many times the elevator was going up then started going down and vice versa.

Help chef by answering his question or determine that the sequence B is invalid.

Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two integers N and M.
The second line contains N space-separated integers B1,B2,…,BN.
Output:
For each test case, print a single line containing one integer ― the minimum number of times the elevator has changed its direction or −1 if the given B sequence is invalid.

Constraints
1≤T≤1000
1≤N≤105
2≤M≤105
1≤Bi≤M or Bi=−1 for each valid i
sum of N over all test-cases doesn't exceed 106
Subtasks
Subtask #1 (50 points):

N≤1,000
the sum of N over all test cases does not exceed 10,000
Subtask #2 (50 points): Original constraints

Sample Input:
5
4 5
2 3 4 3
4 5
2 -1 4 3
4 5
1 -1 -1 5
5 4
-1 -1 3 -1 -1
5 5
-1 -1 3 -1 -1
Sample Output:
1
1
-1
1
0
Author:	6★kingofnumbers
Date Added:	28-08-2020
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ
Submit

"""