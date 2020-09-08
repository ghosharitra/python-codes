
def sol(target):
    b=[10,7,5,1]
    res=0
    for i in range(4):
        if(target>=b[i]):
            res=res+target//b[i]
            target=target%b[i]
    return res

target=[]
try:
    t=int(input())
    for i in range(t):
        target.append(int(input()))
except:
    print("-1")
    exit(0)

for i in range(t):
    res=sol(target[i])
    print(res)