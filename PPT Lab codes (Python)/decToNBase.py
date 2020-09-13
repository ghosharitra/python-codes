def decToNBase(num,n):
    s=""
    while(num>0):
        x=num%n

        if(x>9):
            x=chr(x-10+65)
        else:
            x=str(x)
        
        s=x+s
        num=num//n
    return s

print(decToNBase(int(input()),int(input())))