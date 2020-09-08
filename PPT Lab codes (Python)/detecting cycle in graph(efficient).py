# NOT COMPLETE
# (tried making efficient loop detecting algo 
# by memorizing paths with no loop, ended up failing)

def sol(graph,n,l=0,node=-1,head=-1):
    
    if memory[i]!=0:
        return False

    if l!=0:   
        
        for j in range(n):
            if(graph[node][j]==1 and j!=head):
                if(selected[j]==1):
                    return True
                selected[j]=1
                flag=sol(graph,n,l+1,j,node)
                selected[j]=0
                if(flag==True):
                    return flag

                memory[node]=memory[node]+[j]+memory[j]
                
        return False

    elif l==0:
        for i in range(n):
            selected[i]=1
            if memory[i]!=0:
                continue        
            
            for j in range(n):
                
                if(graph[i][j]==1):
                    if(selected[j]==1):
                        return True
                    selected[j]=1
                    flag=sol(graph,n,l+1,j,i)
                    selected[j]=0
                    memory[i]=memory[i]+memory[j]
                    if(flag==True):
                        return flag
            selected[i]=0
        return False








info=[]
graph=[]

edge=int(input())
n=int(input())
memory=[0]*n
selected=[0]*n
for i in range(n):
    temp=[0]*n
    graph.append(temp)

for _ in range(edge):
    i,j=map(int,input().split()[0:2] )
    graph[i][j]=1
    graph[j][i]=1

print()
for i in range(n):
    print(graph[i])

flag,cycle=sol(graph,n)

