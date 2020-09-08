"""
ARRAY Q8)
Given an unsorted array of positive integers, find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any of the two values (or sides) must be greater than the third value (or third side).

Examples:

Input: arr= {4, 6, 3, 7}
Output: 3
Explanation: There are three triangles 
possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. 
Note that {3, 4, 7} is not a possible triangle.

"""

def sol(sides,n,l=0,index=0,tri=[0]*3):
    if(l==3):
        #print(tri)
        if (tri[0]+tri[1])>tri[2] and (tri[2]+tri[1])>tri[0] and (tri[0]+tri[2])>tri[1]:
            return 1
        return 0
    res=0
    for i in range(index,l+n-3+1):
        tri[l]=sides[i]
        res=res+sol(sides,n,l+1,i+1,tri)
    #print("l:",l,"res:",res)
    return res





sides=list(map(int,input().split()))
res=sol(sides,len(sides))

print(res)