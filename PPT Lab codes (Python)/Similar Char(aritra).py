try:
    m=int(input())
    string=input()
    if m!=(len(string)):
        raise Exception
    n=int(input())
    no=list(map(int,input().split()))
    if n!=len(no):
        raise Exception
except:
    print("wrong input")
    exit(0)
for i in range(n):
    c=0
    value=string[no[i]-1]
    cut=" "
    cut=string[0:(no[i]-1)]
    for j in range(len(cut)):
        if value==cut[j]:
            c+=1
    print(c)