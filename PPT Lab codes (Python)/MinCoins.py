"""
Find the minimum number of coins required to form the value.

"""

d={}


def mincoins(n):
    print("n:",n)
    coins=[7,5,3]

    if n==0:
        return 0

    res=99999
    for i in coins:
        
        if(n-i>=0):
            if((n-i) in d):
                subres= d[n-i]+1
            else:
                subres=mincoins(n-i)+1
            
            if(res>subres):
                res=subres

    print("n:",n,"res:",res)
      
    d[n]=res
    return res



n=int(input())
res=mincoins(n)
if(res==99999):
    res=-1  
print(res)