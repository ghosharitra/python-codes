def isPrime(n):
    if(n<2):
        return False
    elif(n==2):
        return True
    elif(n%2==0):
        return False
    else:
        for i in range(3,int(n**(1/2))+1,2 ):
            if(n%i==0):
                return False
        else:
            return True


x=isPrime(int(input("enter number to check prime or not:")))
print(x)