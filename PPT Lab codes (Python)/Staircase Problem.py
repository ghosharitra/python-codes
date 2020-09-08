"""
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time.

Count the number of ways, the person can reach the top.

"""
def sol(n,x=0,res=0):
    if(n<x):
        return res
    if(n==x):
        res+=1
        return res
    
    res=sol(n,x+1,res)
    res=sol(n,x+2,res)    

    return res


n=int(input())
res=sol(n)
print(res)
