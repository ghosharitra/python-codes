def merge(a,b):
    arr=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
       if a[i]<b[j]:
           arr.append(a[i])
           i+=1
       else:
           arr.append(b[j])
           j+=1

    for k in range(i,len(a)):
        arr.append(a[i])

    for k in range(j, len(b)):
        arr.append(b[j])

    return arr

def sort(arr):
  if len(arr)==1:
      #print("arr=",arr)
      return arr
  else:
        mid=(len(arr))//2
        #print("mid= ",mid)
        #print("arr[:mid]= ", arr[:mid])
        #print("arr[mid:]= ",arr[mid:])

        a=sort(arr[:mid])
        b=sort(arr[mid:])
        arr= merge(a,b)
        #print(arr)
        return arr



l=[5,3,7,5,4,7,6,2,5,1,3,5,42,5,2,5,2,65,58,2,6,5,6,2,56,2,36,6]
x=sort(l)
print(x)