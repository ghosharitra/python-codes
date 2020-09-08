x=input()
y=input()

l=[]

for i in range(len(x)):
    if x[i] not in y:
        l.append(x[i])
    else:
        #print("hi")
        y=y.replace(x[i],"",1)
#print(x)
    
for i in range(len(y)):
    if y[i] not in x:
        l.append(y[i])
    else:
        #print("ho")
        x=x.replace(y[i],"",1)
#print(y)
#print(l)
print("no. to be removed: ",len(l))








"""a=list(input())
a.sort()
#print(a)

b=list(input())
b.sort()
#print(b)
i=0
while i<len(a):
  j=0
  while j<len(b):
    if a[i]==b[j]:
      del a[i]
      del b[j]
      i-=1
      j-=1
      break
    j=j+1
  i=i+1
#print(a) 
#print(b) 
print(len(a)+len(b))


"""