"""
Critical Planets
Problem Description
War between Republic and Separatist is escalating. The Separatist are on a new offensive. They have started blocking the path between the republic planets (represented by integers), so that these planets surrender due to the shortage of food and supplies. The Jedi council has taken a note of the situation and they have assigned Jedi Knight Skywalker and his Padawan Ahsoka to save the critical planets from blockade (Those planets or system of planets which can be accessed by only one path and may be lost if that path is blocked by separatist).
Skywalker is preparing with the clone army to defend the critical paths. He has assigned Ahsoka to find the critical planets. Help Ahsoka to find the critical planets(C) in ascending order. You only need to specify those planets which have only one path between them and they cannot be accessed by any other alternative path if the only path is compromised.
Constraints
M <= 10000
N <= 7000
Input
First line contains two space separated integers M and N, where M denotes the number of paths between planets and N denotes the number of planets.
Next M lines, each contains two space separated integers, representing the planet numbers that have a path between them.
Output
C lines containing one integer representing the critical planet that they need to save in ascending order of the planet number if no planet is critical then print -1
Time Limit
1
Examples
Example 1
Input
3 4
0 1
1 2
2 3
Output
0
1
2
3
Explanation
 
Since all the planets are connected with one path and cannot be accessed by any alternative paths hence all the planets are critical.
Example 2
Input
7 6
0 2
0 1
1 2
2 3
4 5
3 4
3 5
Output
2
3
Explanation
 
If the republic loose the path between 2 and 3 then the two system of planets will not be able to communicate with each other. Hence 2 and 3 are critical planets.


"""
"""
input:
5 4
0 1
1 2
2 0
2 3
3 0

"""


edgeset=[]
def sol(graph,n,loops,l=0,node=0,head=-1,):
    #print("l:",l,"head:",head,"node:",node,"selected:",selected)
 
    if selected[node]==1:
        c=0
        for e in edgeset:
            if(e[0]==node):
                break
            c+=1

        loops+=edgeset[c:].copy()
        
        return 
    
    selected[node]=1
    
    for j in range(n):                              
            if graph[node][j]==1 and j!=head and j!=node:# j!=node <-- THIS CONDITION IS PRESENT SO THAT IT DOESN'T COUNT SELF LOOP
                #print(">>l:",l,"head:",head,"node:",node,"selected:",selected)
                edgeset.append([node,j])
                sol(graph,n,loops,l+1,j,node)
                edgeset.pop()

        
    selected[node]=0
    return 
 








info=[]
graph=[]
loops=[]
edges=[]
edge,n=map(int,input().split()[0:2] )

selected=[0]*n

for i in range(n):
    temp=[0]*n
    graph.append(temp)

for _ in range(edge):
    i,j=map(int,input().split()[0:2] )
    graph[i][j]=1
    graph[j][i]=1
    edges.append([i,j])

# print()
# for i in range(n):
#     print(graph[i])

sol(graph,n,loops)

#print("loops:",loops)

cut=[]
for e in edges:
    if e not in loops:
        cut.append(e[0])
        cut.append(e[1])

cut=list(set(cut))
if len(cut)==-0:
    print("-1")
else:
    for i in cut:
        print(i)