n=int(input())
seq=list(map(int,input().strip().split()))

result=[]
temp=[ seq[0] ]
lpslen=0
count=1
i=1
while (i<n):


    if seq[i]<temp[-1]:
        if(lpslen<count):
            lpslen=count
            result=temp.copy()

        
        temp=[ seq[i] ]
        count=1


    else:
        temp.append(seq[i])
        count=count+1
        #print("->",temp)
    i=i+1

if(lpslen<count):
    lpslen=count
    result=temp.copy()


print(result)