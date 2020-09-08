"""
(a^b)%c=?

"""

def sol(a,b,c):
    print("a:",a,"b:",b,"c:",c)
    if(b==0):
        return 1
    if(b & 1==0):
        print("b%2==0")
        return sol(((a%c)*(a%c))%c,b>>1,c)%c
    return a*sol(a,b-1,c)%c


a,b,c=map(int,input().split() )
res=sol(a,b,c)
print(res)
