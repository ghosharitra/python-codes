l=[]
n = int(input("enter size of list: "))

print("enter elements: ")
for i in range(n):
    l.append(int(input()))

x=[]
for i in l:
    if i not in x:
        x.append(i)

print("unique list: ",x)