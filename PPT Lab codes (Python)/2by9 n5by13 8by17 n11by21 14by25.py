n=int(input())
l=['2/9']

for i in range(1,n):
  x=abs(int(l[i-1].split("/")[0]))
  y=int(l[i-1].split("/")[1])
  if i%2==0:
    l.append(str(x+3)+"/"+str(y+4))
  else:
    l.append(str(-(x+3))+"/"+str(y+4))
 
print (l[:n])