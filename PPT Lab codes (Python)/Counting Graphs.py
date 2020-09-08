"""
One day, Tanya was studying graph theory. She is very inquisitive, so the following problem soon came to her mind.

Find the number of undirected unweighted connected simple graphs with N vertices (numbered 1 through N) and M edges, such that for each i (2≤i≤N), the shortest path from vertex 1 to vertex i is unique and its length is equal to Ai. In other words, for each i (2≤i≤N), there should be exactly one path with length Ai between vertices 1 and i, and there should be no paths with smaller length between these vertices.

Two graphs with N vertices are distinct if we can find two vertices u and v such that there is an edge between these vertices in one graph, but not in the other graph.

Since the answer could be very large, compute it modulo 1,000,000,007 (109+7).

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M.
The second line contains N−1 space-separated integers A2,A3,…,AN.
Output
For each test case, print a single line containing one integer ― the number of graphs modulo 109+7.

Constraints
1≤T≤1,000
2≤N≤105
N−1≤M≤min(2⋅105,N(N−1)2)
1≤Ai≤N−1 for each valid i
the sum of N over all test cases does not exceed 2⋅105
the sum of M over all test cases does not exceed 2⋅105
Subtasks
Subtask #1 (50 points): M=N−1
Subtask #2 (50 points): original constraints

Example Input
3
4 3
1 2 1
4 6
1 2 1
3 2
2 2
Example Output
2
0
0
Explanation
Example case 1: The two graphs which satisfy all conditions are:  

Author:	5★sawarnik123
Date Added:	23-08-2020
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ
Submit

"""