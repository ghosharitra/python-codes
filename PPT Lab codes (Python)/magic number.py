def sol(n):
    s=n%9
    if(s==0):
        s=9
    if(s==1):
        print("magic number")
    else:
        print("not magic number")

try:
    n=int(input())
except:
    print("Invalid Input")
    exit(0)
sol(n)
