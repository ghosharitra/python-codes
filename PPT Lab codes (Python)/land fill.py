t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    
    l=list(map(int,input().split()))
    avg=sum(l)/n
    avg=1-(avg-int(avg))
    print(int(avg*n*x))
    