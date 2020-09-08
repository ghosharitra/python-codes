"""
You are given a binary string S with length N and an integer K, which is a divisor of N. A string is said to be K-foldable if it can be changed to a string with length K by repeating the following process without any collisions (defined below):

Select the prefix of the current string S with length 2K. (Note that as long as the length of S is greater than K, this prefix always exists.)
For each i (1≤i≤K), check if the 2K−i+1-th character of S is equal to the i-th character of S ― if they are not equal, there is a collision and the process is invalid.
Erase the prefix of S with length K.
Your goal is to reorder the characters of S (possibly leaving this string unchanged) in such a way that the resulting string S is a K-foldable string. Find a way to do that or determine that it is impossible. If there are multiple solutions, find the lexicographically smallest rearranged string which is K-foldable.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains a single string S with length N.
Output
For each test case, print a single line containing the smallest rearranged string or the string "IMPOSSIBLE" if it is impossible to rearrange S.

Constraints
1≤T≤100
1≤K≤N≤103
N is divisible by K
S contains only characters '0' and '1'
Example Input
2
8 2
00011101
6 2
100111
Example Output
01100110
IMPOSSIBLE
Explanation
Example case 1: If the given string "00011101" is rearranged to "01100110", it becomes 2-foldable:

Initially, S is "01100110".
After the first folding, it becomes "100110".
After the second folding, it becomes "0110".
After the third folding, it becomes "10". This string has length 2, so we are done.
Example case 2: It is impossible to rearrange S into a 2-foldable string.

All submissions for this problem are available.
Author:	5★pandey__ji
Editorial:	https://discuss.codechef.com/problems/KFOLD
Tags:	ad-hoc, cook121, pandey__ji, pandey__ji, psychik, simple, simple-math
Date Added:	16-08-2020
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ

"""

t=int(input())
for _ in range(t):
    #print("in loop1")
    n,foldsize=map( int,input().split() )
    string=input()
    nfolds=n//foldsize
    c0=string.count("0")
    c1=string.count("1")
    
    if c0%nfolds==0 and c1%nfolds==0:
        #print("in if 1")
        val1=c0//nfolds
        val2=c1//nfolds
        #print("nfolds:",nfolds,"c0:",c0,"c1:",c1,"val1:",val1,"val2:",val2)
        if val1+val2==foldsize:
            #print("in if 2")
            fold="0"*val1+"1"*val2
            #print("fold:",fold)
            res=""
            for i in range(nfolds):
                #print("in loop2")
                res=res+fold
                fold=fold[::-1]
            print(res)
        else:
            #print("in else 1")
            print("IMPOSSIBLE")
            continue
    else:
       # print("in else 2")
        print("IMPOSSIBLE")
        continue