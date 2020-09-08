#THIS IS ALSO KNOWN AS SIEVE OF ERATOSTHENES
def primeRange(n):

    prime=[1]*(n+1)
    prime[0]=0
    prime[1]=0

    for i in range(2,int(n**(0.5))+1):
        if(prime[i]!=0):
            for j in range(2*i,n+1,i):
                prime[j]=0

    return prime


n=int(input("enter number to check prime till that no:"))
prime=primeRange(n)
for i in range(n+1): print( i,"\t",prime[i] )

















