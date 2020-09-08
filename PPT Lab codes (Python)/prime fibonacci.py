def prime(n):
  if n==1:
    return False
    
  for i in range(2,int(n/2)+1):
    if n%i==0:
      return False
  #print(n)
  return True
  
  
def pf():
  
  n1=int(input())
  n2=int(input())

  l1=[]
  i=n1
  while i<n2:
    if prime(i):
      l1.append(i)
    i+=1
  print ("l1: ", l1)


  l2=[]
  for i in l1:
    for j in l1:
      if i!=j:
        l2.append(int(str(i)+str(j)))
    
  print ("l2: ", l2)


  l3=[]
  for i in l2:
    if prime(i):
      l3.append(i)
    
  print ("l3: ", l3)

  minimum=min(l3)
  maximum=max(l3)
  fib=[minimum, maximum]
  for i in range(2,len(l3)-2):
    fib.append(fib[i-1]+fib[i-2]) 
  
  print ("prime fibonacci: ", fib) 


#import timeit

#timeit.timeit(pf())