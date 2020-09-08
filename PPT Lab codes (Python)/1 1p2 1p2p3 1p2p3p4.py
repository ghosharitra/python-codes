n=int(input())
s="1"
l=[]
for i in range(2,n+2):
  #print(s)
  l.append(s)
  s=s+"+"+str(i)
  
print(l)