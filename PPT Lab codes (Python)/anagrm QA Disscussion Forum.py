"""
STRINGS Q8)
Given two strings a and b consisting 
of lowercase characters. 
The task is to check whether two given strings 
are anagram of each other or not. 
An anagram of a string is another string that 
contains same characters, only the order of 
characters can be different. 
For example, “act” and “tac” are anagram of each other.

Input:
The first line of input contains an integer T 
denoting the number of test cases. 
Each test case consist of two strings in 'lowercase' 
only, in a single line.

Output:
Print "YES" without quotes if the two strings are 
anagram else print "NO".

Constraints:
1 ≤ T ≤ 300
1 ≤ |s| ≤ 106

Example:
Input:
2
geeksforgeeks forgeeksgeeks
allergy allergic

Output:
YES
NO

Explanation:
Testcase 1: Both the string have same characters with 
same frequency. So, both are anagrams.
Testcase 2: Characters in both the strings are not same, 
so they are not anagrams.

"""

t=int(input())
for _ in range(t):
    letters1={ "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    letters2={ "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

    word1,word2=input().split()

    for i in word1:
        letters1[i]+=1

    for i in word2:
        letters2[i]+=1

    if(letters1==letters2):
        print("YES")
    else:
        print("NO")