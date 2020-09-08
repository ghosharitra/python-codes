"""
Q)8
Given an unsorted array of positive integers, find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any of the two values (or sides) must be greater than the third value (or third side).

Examples:

Input: 
4
4 6 3 7
3
Output:
3 4 6
4 6 7
3 6 7
3 4 7

"""

def sol(sides,n,group,lengroup,l=0,index=0,):
    if(l==lengroup):
        print(group)
        return 

    for i in range(index,l+n-lengroup+1):
        group[l]=sides[i]
        sol(sides,n,group,lengroup,l+1,i+1)
    
    #print("l:",l,"res:",res)
    return 




n=int(input())
arr=list(map(int,input().split()))
lengroup=int(input())
group=[0]*lengroup
sol(arr,n,group,lengroup)
