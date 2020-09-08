def digit(n):
    if n<10:
        return n
    else:
        z=n
        s=0
        while(n>0):
            k=n%10
            s=s+k
            n=n//10
            
        return digit(s)


n=int(input("enter a no."))
print(digit(n))