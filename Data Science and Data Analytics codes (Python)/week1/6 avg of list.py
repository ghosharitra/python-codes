l=[]
n = int(input("enter size of list: "))

print("enter elements: ")
sum=0
for i in range(n):
    l.append(int(input()))
    sum=sum+l[i]
print("average: ",sum/n)