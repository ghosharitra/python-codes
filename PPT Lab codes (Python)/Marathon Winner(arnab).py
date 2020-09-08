try:
    l1=[]
    mat=[]
    res=[]
    n=int(input())
    t=int(input())
    for i in range(n):
        
        l1=list(map(int,input().split()))
        mat.append(l1)
        
        if len(l1)!=t+1:
            raise Exception
        
except:
    print("invalid")
    exit(0)
r1=0
l2=[]
res=[]
#print(mat)
l=len
for i in range(2,t,2):
    
    for k in range(len(mat)):
        for j in range(0,i):
            #print(mat[k][j])
            #print(mat[k][t])
            r1=r1+(mat[k][j]*mat[k][t])
        l2.append(r1)
        r1=0
    m=max(l2)
    #print(l2)
    #print(m)
    for l in range(len(l2)):
        #print(l2[l])
        if l2[l]==m:
            res.append(l)
            
    l2=[]
    #
    print(res)

cf=0
c=0
num=0
            
for i in res:
    cf=res.count(i)
    if cf>c:
        c=cf
        
        num=i
               
print(num+1)