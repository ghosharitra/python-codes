"""
Q)8
Given an unsorted array of positive integers, find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any of the two values (or sides) must be greater than the third value (or third side).

Examples:

Input: 
3
6 3 7
3

Output:
6 3 7
6 7 3
3 6 7
3 7 6
7 3 6
7 6 3

"""

def sol(sides,n,group,lengroup,l=0,index=0,):
    if(l==lengroup):
        print(group)
        return 

    for i in range(n):
        if selected[i]!=1:
            group[l]=sides[i]
            selected[i]=1
            sol(sides,n,group,lengroup,l+1,i+1)
            selected[i]=0

    #print("l:",l,"res:",res)
    return 




n=int(input())
arr=list(map(int,input().split()))
lengroup=int(input())
group=[0]*lengroup
selected=[0]*n
sol(arr,n,group,lengroup)
