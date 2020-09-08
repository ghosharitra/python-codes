p=int(input("enter no. of rows of first matrix: "))
q=int(input("enter no. of columns of first matrix: "))
r=int(input("enter no. of columns of second matrix: "))

x=[]
y=[]
z=[]
print("enter the elements of first matrix:")
for i in range(p):
    t=list(map(int,input().split()[0:q]))
    x.append(t)

print("enter the elements of second matrix:")
for i in range(q):
    t=list(map(int,input().split()[0:r]))
    y.append(t)


for i in range(p):
    t=[]
    for j in range(r):
        t.append(0)
    z.append(t)


print(x)
print(y)
print(z)

for i in range(p):
    for j in range(r):
        s=0
        for k in range(q):
            s=s+x[i][k]*y[k][j]
        z[i][j]=s

for i in range(p):
    for j in range(r):
        print(z[i][j],end=" ")
    print()