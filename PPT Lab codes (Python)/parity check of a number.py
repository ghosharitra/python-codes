x=int(input("enter a number: "))
x=bin(x)[2:]
s=0
for i in x:
    s=s+int(i)

if s%2==0:
    print('0')
else:
    print('1')