array=list(map(int,input().split()))
print(array)
n=len(array)
narray=[]
temp=[array[0]]
for i in range(n-1):
    
    if(abs(array[i+1] - array[i]) <= 2):
        
        temp.append(array[i+1])
    else:
        narray.append(temp)
        temp=[array[i+1]]
narray.append(temp)

print(narray)
        


