#NOT GIVING CORRECT ANS

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
#NOT GIVING CORRECT ANS


di={}


def disp(mat,n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end="\t")
        print("\n")

def detectComp(mat,n,node):
    #print("selected:",selected,"node:",node,"head:",head)
    if(di[node][0]==node):
        for i in range(0,di[node][0]):
            if matrix[node][i]==1:
                di[node]=di[i]
                
                return
        else:
            di[node]=[node]
            return


def evencount(mat,n):
    count=[0]*n
    res=0
    for i in range(n):
        detectComp(mat,n,i)
        count[ di[i][0] ]+=1
    print("dict:",di)
    print("count:",count)

    
    for i in range(n):
        if(count[i]!=0 and count[i]%2==0):
            res+=1
    print("res:",res)
    return res

matrix=[]
try:
    n=int(input())

    for i in range(n):
        temp=[0]*n
        matrix.append(temp)
        di[i]=[i]

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