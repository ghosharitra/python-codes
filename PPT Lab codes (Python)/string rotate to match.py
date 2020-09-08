"""
STRINGS Q7)
Given two strings a and b. The task is to find if a 
string 'a' can be obtained by rotating another 
string 'b' by 2 places.

Input:
The first line of input contains an integer T 
denoting the no of test cases. 
Then T test cases follow. 
In the next two line are two string a and b.

Output:
For each test case in a new line print 1 
if the string 'a' can be obtained by rotating 
string 'b' by two places else print 0.

Constraints:
1 <= T <= 50
1 <= length of a, b < 100

Example:
Input:
2
amazon
azonam
geeksforgeeks
geeksgeeksfor

Output:
1
0

Explanation:
Testcase 1: amazon can be rotated anti-clockwise by two 
places, which will make it as azonam.

Testcase 2: geeksgeeksfor can't be formed by any rotation 
from the given word geeksforgeeks.

"""


t=int(input())
for _ in range(t):
    word1=input()
    word2=input()
    word2=word2[-2:]+word2[:-2]
    
    if(word1==word2):
        print("1")
    else:
        print("0")