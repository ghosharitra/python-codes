t=int(input())

for z in range(t):
  count=0
  s=input()
  #s1=[]
  i=0
  n=len(s)
  while i<n-1:
    #s1.append(s[i])
    if s[i]==s[i+1]:
      j=1
      #count=1
      while True:
        if i+j<n:
          if s[i]==s[i+j]:
            count+=1
          else:
            break
        else:
          break
        j+=1
      #s1.append(count)
      i=i+j-1    
    i=i+1
  #print(s1)
  print(count)
        
        
 