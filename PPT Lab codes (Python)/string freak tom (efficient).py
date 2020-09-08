"""
STRINGS Q1)

Tom is a string freak. He has got sequences of  n 
words to manipulate. 
If in a sequence, two same words come together 
then he’ll destroy each other. 
He wants to know the number of words left 
in the sequence after this pairwise destruction.
 

Input:
The first line of input contains an integer 
denoting the no of test cases. 
Then T test cases follow. 
Each test case contains two lines. 
The first line of input contains an integer n 
denoting the number of words in a sequence. 
In the second line are n space separated 
words of the sequence.
Words are contiguous stretches of printable characters 
delimited by white space.
 

Output:
For each test case in a new line print the number 
of words left per sequence.
 

Constraints:
1<=T<=100
1<=n<=100
 

Example:
Input:
2
5
ab aa aa bcd ab
4
tom jerry jerry tom

Output:
3
0

Explanation:

Test Case 1: ab aa aa bcd ab
After the first iteration, we'll have: ab bcd ab
We can't further destroy more strings and hence we stop 
and the result is 3.

Test Case 2: tom jerry jerry tom
After the first iteration, we'll have: tom tom
After the second iteration: 'empty-array'
Hence, the result is 0.

"""
for _ in range(int(input())):     
    n=int(input())
    stack=[]
    words=input().split()
    res=0
    for word in words:
        if len(stack)>0 and stack[-1]==word:
            stack.pop()
            res-=1
            continue
        stack.append(word)
        res+=1
    print(res)