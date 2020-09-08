n=int(input())

a=1
b=1
c=2

for i in range(n):
    
    if i%2==0:
        #print(a)
        s=a
        x=a+b
        a=b
        b=x

    else:
        #print(c)
        s=c
        while (True):
            #print("c=",c)
            c=c+1
            j=2
            flag=0
            while(c>=j*j):
                if(c%(j)==0):
                    flag=1
                    break
                j=j+1
            if(flag==0):
                break



print(s)

