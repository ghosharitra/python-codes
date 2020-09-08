n=int(input())
l=[2]

for i in range(1,n):
  l.append(l[i-1]+13*i)
 
print (l[:n])