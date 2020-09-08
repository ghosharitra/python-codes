n=int(input())
a=list(map(int,input().split()))
count=0
i=0
while i<n:
  j=i
  k=i
  min=a[i]
  while j<n:
    if min>a[j]:
      min=a[j]
      k=j
    j+=1
      
  if i!=k:
    t=a[i]
    a[i]=a[k]
    a[k]=t
    count+=1
    print(a)
  i+=1
   
print(count)