clas=[]
res=[]
try:
    cl,tot=list(map(int,input().split()))
    t=tot

    for i in range(cl):
        x=int(input())
        clas.append(x)
        
    if len(clas)>cl:
        raise Exception
        
except:
    print("wrong")
    exit(0)
    
clas.sort(reverse=True)
if tot>=sum(clas):
    tot=sum(clas)-1

for i in range(len(clas)):
    if tot>0:
        temp=tot
        tot=tot-clas[i]
        res.append(temp-tot)
print("res=",res)
if tot<0:
    l=len(res)-1
    res[l]=res[l]+tot
    
for i in range(len(res),len(clas)):
    res.append(0)
    
print("res=",res)

print(sum(clas))
if t<=sum(clas)-1:
    print("Thank you, your order for "+ str(t) ," eggs are accepted ")
    for i in range(len(clas)):
        print(clas[i]   ,res[i]   ,clas[i]-res[i])
    
if t>=sum(clas):
    print("Sorry, we can only supply " +str(sum(clas)-1) ," eggs ")
    for i in range(len(clas)):
        print(clas[i]   ,res[i]   ,clas[i]-res[i])