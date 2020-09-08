"""
SAMPLE INPUT
2
5 1 1 1
7 2 3 7

SAMPLE OUTPUT
5
9


"""
#"""
tc=int(input())
for j in range(tc):
    coordinators=list(input()[::2])
    ntask=int(coordinators[0])
    print(coordinators)
    i=1
    count=0
    while count<ntask:
       if (i%int(coordinators[1])==0) or (i%int(coordinators[2])==0) or (i%int(coordinators[3])==0):
           count+=1
       i+=1
    print(i-1)
#"""

"""
tc=int(input())
for j in range(tc):
    coordinators=list(map(int,input().split()))
    ntask=coordinators[0]
    del coordinators[0]
    i=1
    count=0
    while count<ntask:
       if i%coordinators[0]==0 or i%coordinators[1]==0 or i%coordinators[2]==0:
           #print(i)
           count+=1
       i+=1
    print(i-1)

"""