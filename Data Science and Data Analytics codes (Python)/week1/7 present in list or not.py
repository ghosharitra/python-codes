l=[]
n = int(input("enter size of list: "))

print("enter elements: ")
for i in range(n):
    l.append(int(input()))
x = int(input("enter a number: "))
if x in l:
    print(x,"is present in the list")
else:
    print(x, "is not present in the list")