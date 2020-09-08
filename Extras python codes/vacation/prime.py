x = int(input("enter a number: "))
#f = 1
# using normal for loop
#for i in range(2, x):
#    if x % i == 0:
#        f = 0
#        break

#if f == 1:
#    print(x, " is prime")
#else:
#    print(x, " is not prime")

#using for else loop

for i in range(2, x):
    if x % i == 0:
        print(x, " is not prime")
        break

else:
    print(x, " is prime")
