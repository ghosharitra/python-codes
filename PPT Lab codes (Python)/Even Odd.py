"""
Problem Description
Given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.

Calculate the number of all such permutations.

As this number can be large, print it modulo (1e9 +7).

Constraints
0 <= low <= high <= 10^9

K <= 10^6.

Input
First line contains two space separated integers denoting low and high respectively

Second line contains a single integer K.

Output
Print a single integer denoting the number of all such permutations

Time Limit
1

Examples
Example 1

Input

4 5

3

Output

4

Explanation

There are 4 valid permutations viz. {4, 4, 4}, {4, 5, 5}, {5, 4, 5} and {5, 5, 4} which sum up to an even number

Example 2

Input

1 10

2

Output

50

Explanation

There are 50 valid permutations viz. {1,1}, {1, 3},.. {1, 9} {2,2}, {2, 4},... {2, 10} . . . {10, 2}, {10, 4},... {10, 10}. These 50 permutations, each sum up to an even number.

"""
di={}
def sol1(l,h,k,count=0,sum=0):
    #print("count:",count,"state:",state,"sum:",sum)
    if(sum in di.keys()):
        return di[sum]
    if(count==k):
        
        if(sum%2==0):
            
            #print(">>>sum:",sum,"ret=1")
            return 1
        else:
            #print(">>>sum:",sum,"ret=0")
            
            return 0

    res=0
    for i in range(l,h+1):
        res=res+sol1(l,h,k,count+1,sum+i)
        res=res%1000000007

    #print(">>>res:",res)
    di[sum]=res
    return res







try:
    l,h=map(int,input().split())
    k=int(input())
    if(l<0 or l>h or h>10**(9) or k>10**(6)):
        raise Exception
except:
    exit(0)


res=sol1(l,h,k)


print(res,end="")
