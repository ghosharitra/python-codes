

def sol(graph,n,l=0,node=-1,head=-1):
    print("l:",l,"node:",node,"head:",head,"selected:",selected)

    if l!=0:   
        if selected[node]==1:
            return True
        
        selected[node]=1
        
        for j in range(n):                              
                if graph[node][j]==1 and j!=head and j!=node:# j!=node <-- THIS CONDITION IS PRESENT SO THAT IT DOESN'T COUNT SELF LOOP
                    print(">>l:",l,"node:",node,"head:",head,"selected:",selected)
                    
                    flag=sol(graph,n,l+1,j,node)

                    if(flag==True):
                        return flag
            
        selected[node]=0
        return False

    elif l==0:
        for i in range(n):
            flag=sol(graph,n,l+1,i)
            if flag==True:
                return flag   
        return False








info=[]
graph=[]

edge,n=map(int,input().split()[0:2] )

selected=[0]*n

for i in range(n):
    temp=[0]*n
    graph.append(temp)

for _ in range(edge):
    i,j=map(int,input().split()[0:2] )
    graph[i][j]=1

print()
for i in range(n):
    print(graph[i])

flag=sol(graph,n)
if flag:
    print("loop detected")
else:
    print("no loop")

