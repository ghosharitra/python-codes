"""
In a social network, online communities refer to the group of people with an interest towards the
same topic. People connect with each other in a social network. A connection between
Person I and Person J is represented as C I J. When two persons belonging to different
communities connect, the net effect is merger of both communities which I and J belonged to.
We are only interested in finding out the communities with the member count being an even
number. Your task is to find out those communities.
Input Format:
Input will consist of three parts, viz.
1. The total number of people on the social network (N)
2.Queries
• C I J, connect I and J
• Q 0 0, print the number of communities with even member-count
-1 will represent end of input.
Output Format:
For each query Q, output the number of communities with even member-count 

Constraints:
1<=N<=10^6
1<=I, J<=N
Sample Input and Output
Input   Output
5
Q 0 0   0
C 1 2   1
Q 0 0   0
C 2 3   1
Q 0 0
C 4 5
Q 0 0
-1
 
"""
def disp(mat,n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end="\t")
        print("\n")

def detectComp(mat,n,selected,node,comp,head=-1,):
    #print("selected:",selected,"node:",node,"head:",head)
    
    if selected[node]==1:
        return
    else:
        comp.append(node)
        #print("comp:",comp)
        selected[node]=1

    for i in range(n):
        
        if mat[node][i]==1 and i!=head and node!=head:
            #print(">>>head:",head,"node:",node,"next:",i)
            detectComp(mat,n,selected,i,comp,node)
    return comp


def evencount(mat,n):
    selected=[0]*n
    count=0
    for i in range(n):
        if selected[i]==0:
            comp=detectComp(mat,n,selected,i,[])
            print("evencount:",comp)
            if(len(comp)%2==0):
                count+=1
    print("count:",count)
    return count

matrix=[]
try:
    n=int(input())
    for i in range(n):
        temp=[0]*n
        matrix.append(temp)

    while True:
        s=input()
        if(s=="-1"):
            break

        elif(s[0]=="C"):
            s=list(map(int,s.split()[1:] ))
            matrix[ s[0]-1 ][ s[1]-1 ]=1
            matrix[ s[1]-1 ][ s[0]-1 ]=1
            disp(matrix,n)
        elif(s=="Q 0 0"):
            print(evencount(matrix,n))
        else:
            raise Exception
except:
    print("Invalid Input")
    exit(0)