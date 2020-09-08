"""
STRINGS Q10)
Your friend is new to programming. 
He is given a task in the school to find the 
total number of alphabets in camel case in a string S. 
Help your friend in doing so.

Input: 
The first line of input contains an integer T, 
denoting the number of testcases. 
For each testcase there will be single line 
containing string S as an input.

Output: 
For each testcase in a new line, 
print the count of camel case character in the string.

Constraints:
1 <= T <= 15
1 <= |S| <= 100

Example:
Input : 
3
ckjkUUYII
HKJT
njnnk

Output : 
5
4
0

Explanation:
Testcase 1: The camel case characters present in 
the given string are: 'U', 'U', 'Y', 'I', 'I'. 

"""

for _ in range(int(input())):
    s=input()
    res=0
    for i in s:
        #print(ord(i))
        if 65<=ord(i) and ord(i)<=90:
            res+=1
    print(res) 