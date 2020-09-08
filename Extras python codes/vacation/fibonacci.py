
def fibfor(n):
    a=0
    b=1
    if n<=0:
        print("invalid number")
    elif n==1:
        print(a)
    elif n >=2:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
    print()


def fibtill(n):
    a = 0
    b = 1

    if n < 0:
        print("invalid number")
    elif n == 0:
        print(a)
    elif n >= 1:
        print(a, end=" ")
        print(b, end=" ")
        c=a+b
        while c<=n:
            print(c, end=" ")
            c = a + b
            a = b
            b = c
    print()


x=int(input("enter no. of terms: "))
fibfor(x)
x=int(input("enter till which no: "))
fibtill(x)