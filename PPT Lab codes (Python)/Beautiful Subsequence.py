"""
Consider a sequence with an even length 2L. A left rotation consists of moving the first element of the sequence to the end. The sequence is good if it is possible to perform some number of left rotations (possibly zero) and divide the resulting sequence into two halves (containing the first L and last L elements respectively) such that the smallest value in one half is greater then the largest value in the other half.

You are given a sequence A1,A2,…,AN. Find the number of its non-empty contiguous subsequences with even length which is good.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing one integer ― the number of good contiguous subsequences.

Constraints
1≤T≤103
1≤N≤105
1≤Ai≤109 for each valid i
A1,A2,…,AN are pair-wise distinct
the sum of N over all test cases does not exceed 106
Example Input
3
4
1 2 3 4
4
4 2 1 3
4
1 3 2 4
Example Output
4
4
3
Explanation
Example case 1: The good subsequences are [1,2], [2,3], [3,4] and [1,2,3,4].

Example case 3: The good subsequences are [1,3], [3,2] and [2,4].

All submissions for this problem are available.
Author:	5★rishup_nitdgp
Editorial:	https://discuss.codechef.com/problems/CHEFHALF
Tags:	ad-hoc, cook121, maths, medium, psychik, rishup_nitdgp, rishup_nitdgp
Date Added:	16-08-2020
Time Limit:	2.5 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ

"""