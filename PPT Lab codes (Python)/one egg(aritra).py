def cal(c,classegg,o):
    #print("cal 1")
    temp2=[]
    for j in range(len(c)):
        temp=[]
        if o<c[j] or j==len(c)-1:
            temp.append(c[j])
            temp.append(c[j]-1)
            temp.append(1)
            
            
        else:
            o=o-c[j]
            temp.append(c[j])
            temp.append(c[j])
            temp.append(0)
            
        temp2.append(temp)
    #print("cal 2")
    print("temp2:",temp2)
    for i in range(len(c)):
        for j in range(len(c)):
            if classegg[i]==temp2[j][0]:
                print(temp2[j])
                temp2[j][0]=0
                break
    #print("cal 3")

def cal2(c,classegg,o):
    temp2=[]
    for i in range(len(c)):
        temp=[]
        if o>c[i]:
            o=o-c[i]
            temp.append(c[i])
            temp.append(c[i])
            temp.append(0)
        elif o<=0:
            temp.append(c[i])
            temp.append(0)
            temp.append(c[i])
        else:
            m=c[i]-o
            
            
            temp.append(c[i])
            temp.append(o)
            temp.append(m)
            o=0
        temp2.append(temp)
    print("temp2:",temp2)
    print("classegg:",classegg)
    for i in range(len(c)):
        for j in range(len(c)):
            if classegg[i]==temp2[j][0]:
                print(temp2[j])
                temp2[j][0]=0
                break


sum=0
c=[]
classegg=[]
n,o=map(int,input().split())
for i in range(n):
    classegg.append(int(input()))
print(classegg)
for i in range(len(classegg)):
    c.append(classegg[i])
c.sort(reverse=True)
print(c)
print(classegg)
for i in range(len(classegg)):
    sum+=classegg[i]
if sum<o:
    print("Sorry,we can only supply ",sum-1," eggs")
else:
    print("Thank you ,your order for ",o," eggs are accepted")
if sum<o:
    cal(c,classegg,o)
else:
  cal2(c,classegg,o)