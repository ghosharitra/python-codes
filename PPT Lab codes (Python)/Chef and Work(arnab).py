t=int(input())
w=[]
n=[]
for i in range(t):
    k=list(map(int,input().split()))
    n.append(k)
    temp=list(map(int,input().split()))[:k[0]]
    w.append(temp)
        
        
#print(w)

for i in range(t):
    sum=0
    c=1
    flag=0
    for j in range(len(w[i])):
        #print(w[i][j])
        if w[i][j]>n[i][1]:
            print('-1')
            flag=1
            break

        if sum+w[i][j]<=n[i][1]:
            sum=sum+w[i][j]
            

        else:
            c+=1
            sum=w[i][j]
    
    if flag!=1:
        print(c)