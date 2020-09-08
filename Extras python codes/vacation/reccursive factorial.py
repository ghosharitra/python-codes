def fact(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)


x = int(input("enter a no: "))
result = fact(x)
if(result!=0):
    print(result)
else:
    print("invalid no.")