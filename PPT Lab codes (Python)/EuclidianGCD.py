def euclidianGCD(a,b):
    if b==0:
        return a
    return euclidianGCD(b,a%b)


a,b=map(int,input().split())
print( euclidianGCD(a,b) )