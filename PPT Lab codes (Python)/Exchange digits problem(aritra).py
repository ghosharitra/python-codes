def sol(a,b):
    c=a.copy()
    c.sort()
    
    print(a)
    print(b)
    print(c)
    d=[]
    for j in range(1,len(b)):
        for i in range(len(a)):
            if c[i]!= -1 and c[i]>=b[len(b)-j]:
                
                d.append(c[i])
                c[i]=-1
                
                print("c=",c)
                break
            c.sort()
            
    d.append(c[len(c)-1])
    print(d)
try:
    n,m=map(int,input().split())
    a=[]
    b=[]
    while n>0:
        k=n%10
        a.append(k)
        n=n//10
    while m>0:
        k=m%10
        b.append(k)
        m=m//10
    if len(a)<len(b):
        raise Exception

except:
    print(-1)
    exit(0)
sol(a,b)