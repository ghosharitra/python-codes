no=int(input())
time=int(input())
temp2=[]
for i in range(no):
    temp=list(map(int,input().split()))
    temp2.append(temp)
a=[]
res=[]
b=[]
for i in range (no):
    res.append(0)
    b.append(0)
print(res)
for i in range(no):
    a.append(temp2[i][time])
for i in range(1,time-2,2):
    for j in range(no):
        temp2[j][i]=temp2[j][i]*a[j]+temp2[j][i-1]*a[j]
        b[j]+=temp2[j][i]
    x=max(b)
    
        
        #print("x",x)
    for j in range(no):
        #print("temp2[j][i]",temp2[j][i])
        if x==b[j]:
            res[j]+=1
    print("b=",b)
    

print("res",res)
z=max(res)
for i in range(len(res)):
    if z==res[i]:
        print(i+1)