def cal(sam,ran,l,ranges,x):
    if l==ranges:
        print(x)
        return
    else:
        #for i in range(ran[l][0],ran[l][1]):
        c=0
        for j in range(len(sam)):
            if sam[j]>ran[l][0] and sam[j]<ran[l][1]:
                c+=1
        x.append(c)
        cal(sam,ran,l+1,ranges,x)

try:
    x=[]
    samples,ranges=map(int,input().split())
    sam=list(map(int,input().split()))
    if samples<len(sam):
        raise Exception
    ran=[]
    for i in range(ranges):
        temp=list(map(int,input().split()))
        if len(ran)>2:
            raise Exception
        ran.append(temp)
except:
    print("invalid input")
    exit(0)
cal(sam,ran,0,ranges,x)