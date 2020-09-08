def isPrime(n):

    if n<2:
        #print("if 1")
        return False
    if n==2:
        #print("if 2")
        return True
    if n%2==0:
        #print("if 3")
        return False

    root=int(n**(0.5))+1
    #print("root:",root)
    for i in range(3,root,2):
        #print("i=",i)
        if(n%i==0):
            #print("if 4")
            return False
    else:
        #print("if 5")
        return True








n=int(input())

sum=5
p=3
count=0
while (sum<n):
    count+=1
    #print("count:",count)
    while True:
        p=p+2
        if(isPrime(p)):
            sum=sum+p
            #print("sum:",sum)
            if(sum>=n):
                break
            if(isPrime(sum)):
                break
        

print(count)