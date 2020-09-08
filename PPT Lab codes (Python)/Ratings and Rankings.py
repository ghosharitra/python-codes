"""

Chef organised a chess tournament, which spanned over M months. There were N players, and player i was rated Ri before the start of the tournament. To see the progress of the players, he noted their rating changes at the end of each month.

After the tournament, FIDE asked Chef to find the number of players whose peak rating and peak ranking did not occur in the same month. In other words, Chef was asked to find the ratings and ranking of each player after each of the M months. Then, using this data, he should find the number of players, such that the month in which they achieved their highest rating over all the months, was different from the month in which they achieved their best rank (based on ratings), over all the months. Note that we do not consider the initial rating/ranking, but only the rating and rankings after each of the M months.

For a particular player, if there are multiple peak rating or peak ranking months, Chef was to consider the earliest of them. If multiple players had the same rating at the end of some month, they were to be given the same rank. For example, if there were 5 players, and their ratings at the end of some month were (2600, 2590, 2600, 2600 and 2590), players 1, 3 and 4 were to be given the first rank, while players 2 and 5 should be given the fourth rank.

As Chef hates statistics, he asks you, his friend, to help him find this. Can you help Chef?

Input:
The first line contains an integer T, the number of test cases.
The first line of each test case contains two space-separated integers N and M, the number of players and the number of months that the tournament spanned over.
The second line of each test case contains N space-separated integers, R1,R2,…,RN denoting the initial ratings of the players, i.e., their ratings before the start of the tournament.
The next N lines each contain M space-separated integers. The jth integer of the ith line, Ci,j denotes the rating change of the ith player after the jth month.
Output:
For each test case, print the number of players whose peak ratings did not occur in the same month as their peak ranking, in a new line.

Constraints
1≤T≤10
1≤N,M≤500
1800≤Ri≤2800
−20≤Ci,j≤20
Subtasks
30 points : 1≤N,M≤50
70 points : Original constraints.
Sample Input:
2
3 3
2500 2500 2520
10 -5 -20
10 15 20
-15 17 13
2 3
2125 2098
-20 10 -10
10 10 -20
Sample Output:
2
2
Explanation:
Test case 1:

The ratings for player 1 after each month are: (2510, 2505 and 2485), while his rankings are first, third and third, respectively. Thus, his best rating and best ranking occur after the same month, i.e., after the first month.

The ratings for player 2 after each month are: (2510, 2525 and 2545), while his rankings are first, first and first, respectively. His best rating occurs after the third month, while his best ranking occurs after the first month (we consider the first month even though his peak ranking is over all the months, because we consider only the earliest month where he attains the peak ranking).

The ratings for player 3 after each month are: (2505, 2522 and 2535), while his rankings are third, second and second, respectively. His best rating occurs after the third month, while his best ranking occurs after the second month.

So there are two players (2 and 3), whose peak ratings did not occur in the same month as their peak ranking, and hence the answer is 2.

Author:	akash_adm
Date Added:	29-08-2020
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP14, C, JAVA, PYTH 3.6, PYTH, CS2, ADA, PYPY, PYP3, TEXT, CPP17, PAS fpc, RUBY, PHP, NODEJS, GO, TCL, HASK, PERL, SCALA, kotlin, BASH, JS, PAS gpc, BF, LISP sbcl, CLOJ, LUA, D, R, CAML, rust, ASM, FORT, FS, LISP clisp, SQL, swift, SCM guile, PERL6, CLPS, WSPC, ERL, ICK, NICE, PRLG, ICON, PIKE, COB, SCM chicken, SCM qobi, ST, NEM, SQLQ
Submit

"""


for _ in range(int(input())):
    n,m=map(int,input().split())
    rating=list(map(int,input().split()))
    data=[]
    for i in range(n):
        temp=list(map(int,input().split()))
        data.append(temp)

    for i in range(n):
        print(data[i])



    for i in range(m):
        for j in range(n):
            if(i==0):
                data[j][i]+=rating[j]
            else:
                data[j][i]+=data[j][i-1]


    for i in range(n):
        print(data[i])

    rank=[]
    for i in range(m):
        info=[]
        info.append( [ [data[j][i],j] for j in range(n) ] )

        info.sort()
        temp=[1]*n
        print("info:",info)
        print("temp:",temp,"\n\n")
        count=1
        for j in range(1,n):
            if info[j][0]==info[j-1][0]:
                temp[ info[j][1] ]=count
            else:
                count+=1
                temp[ info[j][1] ]=count
        rank.append(temp)
        print("temp:",temp,"\n\n")

    for i in range(n):
        print(rank[i])
