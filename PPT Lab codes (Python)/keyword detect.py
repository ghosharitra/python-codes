n=int(input("enter no. of words: "))
print("enter the words:")
inp=[]
for i in range(n):
    inp.append(input())

keys=['if','else','for']

flag=0

for i in range(n):
    for j in keys:
        if inp[i]==j:
            flag=1
            break

    if flag==1:
        print(inp[i], " is a keyword")
        flag=0
    else:
        print(inp[i], " is not a keyword")
        