l=list(map(int,input().split()))
noofcookies=int(l[0])
sweetness=int(l[1])

cookies=list(map(int,input().split()))

cookies.sort()
#print(cookies)

flag=0
count=0
while cookies[0]<sweetness:
  if len(cookies)==1:
    flag=1
    break

  else:
    cookies[1]=cookies[0]+(2*cookies[1])
    del cookies[0]
    cookies.sort()
    #print(cookies)
    count=count+1
if flag==0:
  print(count)
else:
  print(-1)