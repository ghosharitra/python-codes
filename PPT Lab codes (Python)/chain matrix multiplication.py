#input no. of array and the dimensions
n = int(input("enter no. of matrix: "))
dim = list(map(int, input("enter dimensions: ").split()[:n + 1]))


#create multiplication cost matrix initialized with zero
mulcst = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    mulcst.append(temp)

#create split matrix initialized with zero
split = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    split.append(temp)



#print everything
print("dimensions: ",dim)
print("multiplication cost matrix: ",mulcst)
print("split matrix: ",split)

#for separation
print()
print()


#multiplication cost matrix reinitialized with actual values
for d in range(1, n):
    i = 0
    while i + d < n:
        temp = []
        temp1 = []
        for k in range(i, i + d):
            temp.append(mulcst[i][k] + mulcst[k + 1][i + d] + (dim[i] * dim[k + 1] * dim[i + d + 1]))
            temp1.append(k)
        #print the option under the min function
        print("option under the min function: ",temp)
        mulcst[i][i + d] = min(temp)

        split[i][i + d] = temp1[temp.index(min(temp))]

        i += 1


#for separation
print()
print()

#print multiplication cost matrix
for i in range(n):
    for j in range(n):
        print(mulcst[i][j], end="  ")
    print()


#for separation
print()
print()

#print split matrix
for i in range(n):
    for j in range(n):
        print(split[i][j] + 1, end="  ")
    print()



#for separation
print()
print()


#create array of matrix initialized with actual values
matarr=[]

for i in range(n):
    print("enter elements of array ",i+1,':')
    temp2=[]
    for j in range(dim[i]):
        temp1=list(map(int,input().split()[0:dim[i+1]]))
        temp2.append(temp1)
    matarr.append(temp2)


print()
print()
print(matarr)

#multiply two matrices
def matmul(x,y,p,q,r):
    z = []
    for i in range(p):
        t = []
        for j in range(r):
            t.append(0)
        z.append(t)


    for i in range(p):
        for j in range(r):
            s = 0
            for k in range(q):
                s = s + x[i][k] * y[k][j]
            z[i][j] = s

    print("\n\nmatmul result:")
    for i in range(p):
        for j in range(r):
            print(z[i][j], end=" ")
        print()
    return z

#separate group of maritces depending on split matrix recurcively
#multiply the separated resultant matrices
def arrange(i,j):
    if i==j:
        return matarr[i]
    k=split[i][j]
    return matmul(arrange(i,k),arrange(k+1,j),dim[i],dim[k+1],dim[j+1])

print("\n\nfinal multiplication result:\n",arrange(0,n-1))