n=int(input())
temp=n
c=0
star=1
s=""
for i in range(1,n+1):
    s=s+str(i)+str(0)
    c+=1
for i in range((n*n)+1,n*(n+1)+1):
    s=s+str(i)+str(0)
    
d=(n*n)
    
    
    
print(s[:len(s)-1])

st=""   
ss=""

for j in range(temp-1):
    k=0
    for i in range(c+1,(c+1)+(n-1)):
        st=st+str(i)+str(0)
        c+=1
    while k<(n-1):
        ss=str(d)+str(0)+ss
        
        
        
        
        k+=1
        d=d-1
    st=st+ss
    ss=''
    
    
    n=n-1
    print(2*star*'*'+st[:len(st)-1])
    star+=1
    st=''