n=int(input())
l=['1/2']

for i in range(1,n):
  x=int(l[i-1].split("/")[1])
  if i%2==0:
    l.append(str(x)+"/"+str(x+1))
  else:
    l.append(str(-x)+"/"+str(x+1))
 
print (l[:n])