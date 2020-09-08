"""
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time.

Count the number of ways, the person can reach the top.

"""


def sol(n,x=0):
    #print("x:",x,"arr:",arr)
    if(arr[x]!=-1):
        return arr[x]
    if(n<x):
        res=0
        arr[x]=res
        return res
    if(n==x):
        res=1
        arr[x]=res
        return res
    
    res=sol(n,x+1)+sol(n,x+2) 
    arr[x]=res   
    #print("--->>>x:",x,"arr:",arr)
    return res


n=int(input())
arr=[-1]*(n+2)
res=sol(n)
print(arr)
print(res)
