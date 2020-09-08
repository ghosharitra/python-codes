def balloon(v,i,rate):
    if i==1:
        return v
    else:
        m=v-(rate/100)*v
        return balloon(m,i-1,rate)


try:
    sum=0.0
    radius=[]
    n=int(input())
    radius=list(map(float,input().split()))
    rate=float(input())
    radius.sort()
    print(radius)
    if n<len(radius):
        raise Exception
except:
    print("sahi dey bhai")
    exit(0)
radius.sort(reverse=True)
print(radius)
for i in range(len(radius)):
    v=(3.14*radius[i]*radius[i]*radius[i]*4)/3
    maxvolume=balloon(v,i+1,rate)
    print("maxvolume",maxvolume)
    sum+=maxvolume
print('%0.2f'%sum)