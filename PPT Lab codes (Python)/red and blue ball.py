"""

STRINGS Q12)
There is a table on which N balls are kept starting from 
index i=1 to N in horizontal direction.
Each ball is either of "RED" or "BLUE" color.
Make sure that no red ball is placed on even indices and 
no blue ball is placed on odd indices.
Indices in the string start from i=1.

Input:
The first line contains a single integer T 
i.e. the number of test cases.
Then each test case contains a string A which 
consists of either alphabet 'R' for red ball 
or alphabet 'B' for blue ball.

Output:
In one line just print the number of balls placed 
wrong on the table.

 

Constraints:
1<=T<=100
1<=Length of String(N)<=1000

Example:
Input:
3
RRBRBBBR
RBRBRB
BBRRBRB

Output:
6
0
5

Explanation:
Test case 1: 
Alphabet 'R' at positions i=2,4 and 8 is placed 
wrong since 'R' should not be there on even positions. 
Similarly 'B' at positions i=3,5 and 7 is also placed wrong, 
because 'B' should not be there on odd positions.
Hence ans=6.

"""

for _ in range(int(input())):
    balls=input()
    index=1
    res=0

    for ball in balls:
        #print(index , ball)
        if (ball=="R" and index&1==0) or (ball=="B" and index&1==1):
            res+=1
        index+=1

    print(res)











