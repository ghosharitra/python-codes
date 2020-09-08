try:
    holes=int(input())
    holelist=list(map(int,input().split()))
    ball=int(input())
    balllist=list(map(int,input().split()))
    if holes!=len(holelist):
        raise Exception
    if ball!=len(balllist):
        raise Exception
    #balllist.sort()
    res=[]
    
except:
    print("wrong input")
    exit(0)
for i in range(ball):
    res.append(0)

for i in range(holes):
    c=0
    for j in range(ball):
        if holelist[i]>=balllist[j]:
            res[j]=i+1
            c+=1
            if c==i+1:
                break
print(res)
for i in range(holes):
    k=0
    
    for j in range(ball):
        print("i+1=",i+1,"res[j]=",res[j],"k=",k)
        if i+1==res[j]:
            k+=1
            print("->>i+1=",i+1,"res[j]=",res[j],"k=",k)

    if k!=i+1:
        for l in range(ball):
            if holelist[i]>=balllist[l] and res[l]==0:
                    res[l]=i+1
for i in range(len(res)):
    print(res[i],end=" ")