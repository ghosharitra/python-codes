def add(a,b,c):  
        return (a ^ b ^ c),((a & b) | (b & c) | (c & a))

c = int(input("enter no. of bits in dataword: "))
r = int(input("enter no. of datawords: "))

data=[]

for i in range(r):
    temp= list(map(int, list(input())[0:c]))
    data.append(temp)

#print(data)

temp=list(map(int,list('0'*c)))
#print(temp)

zero=list(map(int,list('0'*c)))
#print(zero)

for i in range(r):
    #print("pre: ",temp)
    #print("new: ",data[i])
    cy=0
    for j in range(c-1,-1,-1):
        temp[j],cy=add(data[i][j],temp[j],cy)
    #print("res: ",temp)
    if cy==1:
    #    print("pre: ",temp)
    #    print("new: ",zero)
        for j in range(c-1,-1,-1):
            temp[j],cy=add(temp[j],zero[j],cy)
    #    print("res: ",temp)

temp=list(map(lambda x: int(not x),temp))
print("checksum:",end="")
for i in temp:
    print(i,end="")