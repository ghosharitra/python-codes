"""
ARRAY Q6)
Given a set of n integers, 
divide the set in two subsets of n/2 sizes each 
such that the difference of the sum of two subsets 
is as minimum as possible. 

If n is even, then sizes of two subsets must be 
strictly n/2 and if n is odd, then size of one subset 
must be (n-1)/2 and size of other subset must be (n+1)/2.

For example, let given set be 
{3, 4, 5, -3, 100, 1, 89, 54, 23, 20}, 
the size of set is 10. 
Output for this set should be 
{4, 100, 1, 23, 20} and {3, 5, -3, 89, 54}. 
Both output subsets are of size 5 and sum of elements 
in both subsets is same (148 and 148).

"""

di={}
def sol(arr,n,l=0,part1=0,mindiff=9999999,res=0):
    print("l=",l,"part1=",part1,"mindiff=",mindiff,"res=",res)
    
    if(part1 in di.keys()):
        return res,mindiff
    
    if(part1>res and abs(totalsum-part1-part1)>=mindiff):
        return res,mindiff
    if(l==n//2):
        val=abs(totalsum-part1-part1)
        if(val<mindiff):
            mindiff=val
            res=part1
        print(">>>mindiff=",mindiff,"res=",res)
        return res,mindiff
        
    
    for i in range(n):
        if(select[i]!=1):
            select[i]=1
            res,mindiff=sol(arr,n,l+1,part1+arr[i],mindiff,res)
            select[i]=0
    print("l=",l,"part1=",part1,"mindiff=",mindiff,"res=",res)
    di[part1]=''
    return res,mindiff

n=int(input())
arr=list(map(int,input().split() ))
select=[0]*n
totalsum=sum(arr)

part1,mindiff=sol(arr,n)
part2=totalsum-part1
print(di,"\n\n",part1,part2)