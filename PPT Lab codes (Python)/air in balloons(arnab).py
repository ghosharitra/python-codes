def volume(r):
    v=(4*3.14*r*r*r)/3
    return v


try:
    n=int(input())
    b=list(map(int,input().split()))
    p=int(input())
    b.sort()
    #print(len(b))
    if len(b)>n:
        raise Exception
    
except:
    print("wrong")
    exit(0)
      
#pi=3.14
per=p/100
res=[]
sum=0

for i in range(len(b)):
    v=volume(b[i])
    for j in range(i+1,len(b)):
        
        v=v-(v*per)
        #print(v)
    
    res.append(v)
    
print(res)
for i in range(len(res)):
    sum=sum+res[i]
    
print('%.2f'%sum)