def cal(i,j):
    mul=i*j
    k=i
   
    x=0
    print("i=",i,"j=",j)
    while k*k>=1 and mul>0:
        c=0
        while k*k>mul:
            k-=1
        print("k=",k)
        if int(mul%(k*k))>=0:
            c=int(mul/(k*k))
            mul-=(c*k*k)
        x+=c
       
        print("mul=",mul)
        print("c=",c)
        print("x=",x)
    return x

ll,ul,lb,ub=map(int,input().split())
# ll=int(input())
# ul=int(input())
# lb=int(input())
# ub=int(input())
c=0
for i in range(ll,ul+1):
    for j in range(lb,ub+1):
        x=cal(i,j)
        print("output=",x)
        c+=x
print(c)