#Example Input
#3
#2
#3 6
#3
#1 3 5
#5
#1 2 5 6 7
#Example Output
#1 1
#3 3
#2 3



t = int(input())
while t>0:
    
    n = int(input())
    x = []
    l = []
    a = [int(e) for e in input().split()]
    #x = [a[0]]
    for i in range(n-1):
        if abs(a[i]-a[i+1])<=2:
            x.append(a[i])
        else:
            x.append(a[i])
            l.append(len(x))
            x = []
    x.append(a[-1])
    l.append(len(x))
    print(min(l),max(l))

    t=t-1