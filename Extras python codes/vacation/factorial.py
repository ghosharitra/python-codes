
def fact(n):
    if n<0:
        print("invalid number")
    elif n >=1:
        s=1
        for i in range(1,n+1):
            s=s*i
        print(s)

x=int(input("enter a no: "))
fact(x)
