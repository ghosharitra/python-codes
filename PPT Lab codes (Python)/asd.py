import copy
a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
b=copy.deepcopy(a)



print(a)
print(b)

c=a.copy()
a[0][0]=0


print(a)
print(b)





a[0]=['a','b','c','d']

print(a)
print(c)

d= [[j for j in i] for i in a]
a[0][0]='x'
print(a)
print(d)