"""
STRINGS Q5)
Given a string S, find the longest palindromic 
substring in S. 
Substring of string S: S[ i . . . . j ] 
where 0 ≤ i ≤ j < len(S). 
Palindrome string: A string which reads the 
same backwards. 
More formally, S is palindrome if reverse(S) = S. 
Incase of conflict, return the substring which 
occurs first ( with the least starting index ).

note: Required Time Complexity O(n2).

Input:
The first line of input consists number of the testcases. 
The following T lines consist of a string each.

Output:
In each separate line print the longest palindrome of 
the string given in the respective test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ Str Length ≤ 104

Example:
Input:
1
aaaabbaa

Output:
aabbaa

Explanation:
Testcase 1: The longest palindrome string present in the 
given string is "aabbaa".

"""

for _ in range(int(input())):
    s=input()
    n=len(s)
    substr=[]
    for i in range(n):
        temp=[]
        for j in range(0,i+1):
            if i==j:
                temp.append(1)
            elif(i-1==j):
                if(s[i]==s[j]):
                    temp.append(1)
                else:
                    temp.append(0)
            else:
                temp.append(0)

        substr.append(temp)
    



    for i in range(n):
        print(substr[i])
    



    maxi,maxj,maxdiff=0,0,0
    for i in range(2,n):
        for j in range(i,n):
            #print("i:",i,"j:",j,"   j:",j,"j-i:",j-i,"   s[j]:",s[j],"s[j-i]:",s[j-i],"substr[j-1][j-i+1]:",substr[j-1][j-i+1])
            if(s[j]==s[j-i] and substr[j-1][j-i+1]==1):
                substr[j][j-i]=1
                if((j)-(j-i)>maxdiff):
                    maxdiff=(j)-(j-i)
                    maxi=j
                    maxj=j-i
            else:
                substr[j][j-i]=0


    print("\n\n\n")
    for i in range(n):
        print(substr[i])


    print(maxj,maxi)
    print( s[ maxj:maxi+1 ] )



 