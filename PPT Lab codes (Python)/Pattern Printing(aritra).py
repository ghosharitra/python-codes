n=int(input())
b=[]
k=0
l=n*(n+1)
for i in range(n):
    a=[]
    if i<n:
        m=i*2
        if m!=0:
            for q in range(m):
                a.append("*")
    for j in range(n-i):
       
        a.append(k+1)
        a.append(0)
        k+=1
    
    for j in range(n-i):
        if j!=n-(i+1):
            a.append(l-(n-1-j))
            a.append(0)
        else:
            a.append(l-(n-1-j))

    l=l-n+(i+1)
    b.append(a)
    

s=""
for i in b:
    for j in i:
        s=s+str(j)
    s=s+"\n"
print(s)