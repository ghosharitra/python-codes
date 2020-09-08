n=int(input("enter no. of terms: "))
c=0
for i in range(n):
    if i%2==0:
        print(7*c)
    else:
        print(6*c)
        c += 1



#alternatively

#n=int(input("enter no. of terms: "))
#i=0
#c=0
#while i<n:
#    if i%2==0:
#        print(c)
#    else:
#        print(c-int(i/2))
#        c=c+7
#    i+=1
