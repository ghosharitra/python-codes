n=int(input())
l=[1,3,4]

for i in range(3,n):
  l.append(l[i-1]+l[i-2]+l[i-3])
  
print (l[:n])