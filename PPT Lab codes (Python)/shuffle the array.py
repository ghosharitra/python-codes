"""
Recursion Q6)
Given an array of n elements in the following format 
{ a1, a2, a3, a4, ….., an/2, b1, b2, b3, 
b4, …., bn/2 }. 

The task is shuffle the array to {a1, b1, a2, b2, 
a3, b3, ……, an/2, bn/2 } without using extra space.

Input:
The first line of input contains an integer T 
denoting the number of test cases. 
Then T test cases follow, Each test case contains 
an integer n denoting the size of the array. 
The next line contains n space separated 
integers forming the array.

Output:
Print the shuffled array without using extra space.

Constraints:
1<=T<=10^5
1<=n<=10^5
1<=a[i]<=10^5

Example:
Input:
2
4
1 2 9 15
6
1 2 3 4 5 6

Output:
1 9 2 15 
1 4 2 5 3 6

"""

for _ in range(int(input())):
    n=int(input())
    num=list( map(int,input().split() ))
    x=n//2
    index=1
    for i in range(x,n):
        num=num[:index]+num[i:i+1]+num[index:i]+ num[i+1:]
        index+=2
        print(num)

    
    for i in num:
        print(i,end=" ")