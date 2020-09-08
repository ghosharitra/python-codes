try:
    def cal(temp2,n,l,res):
        if l==n:
            for i in range(l):
                print(res[i],end=" ")
            return
        else:
            c=0
            #temp2[l][0]+=temp2[l][1]
            while temp2[l][0]%temp2[l][2]!=0:
                temp2[l][0]+=temp2[l][1]
                c+=1
                if c>100:
                    raise Exception
            m=int(temp2[l][0]/temp2[l][2])
            res.append(m)
            cal(temp2,n,l+1,res)
except:
    print("it will not match")
    exit(0)




try:
    n=int(input())
    temp2=[]
    res=[]
    for i in range(n):
   # for j in range(0,3):
        temp=list(map(int,input().split()))
        if len(temp)>3:
            raise Exception
        temp2.append(temp)
except:
    print("wrong input")
    exit(0)
cal(temp2,n,0,res)