n=int(input())
l=[1,2]

for i in range(2,n):
  if i%2==0:
    l.append(l[i-1]+l[i-2])
  else:
    l.append(l[i-1]+l[i-2]+l[i-3])
print (l[:n])