"""

Problem : Matrix Rotations

You are given a square matrix of dimension N. Let this matrix be called A. Your task is to rotate A in clockwise direction byS degrees, where S is angle of rotation. On the matrix, there will be 3 types of operations viz. 
Rotation
Rotate the matrix A by angle S, presented as input in form of A S

Querying
Query the element at row K and column L, presented as input in form of Q K L

Updation
Update the element at row X and column Y with value Z, presented as input in form of U X Y Z

Print the output of individual operations as depicted in Output Specification


Input Format:

Input will consist of three parts, viz.
1. Size of the matrix (N)
2. The matrix itself (A = N * N)
3. Various operations on the matrix, one operation on each line. (Beginning either with A, Q or U)

-1 will represent end of input.
Note:
Angle of rotation will always be multiples of 90 degrees only.
All Update operations happen only on the initial matrix. After update all the previous rotations have to be applied on the updated matrix

Output Format:

For each Query operation print the element present at K-L location of the matrix in its current state.

Constraints:

1<=N<=1000
1<=Aij<=1000
0<=S<=160000
1<=K, L<=N
1<=Q<=100000


Sample Input and Output


SNo.	Input	Output
1	    2       3
        1 2     1
        3 4     4
        A 90    6
        Q 1 1
        Q 1 2
        A 90
        Q 1 1
        U 1 1 6
        Q 2 2
        -1	



"""

def disp(mat,n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end="\t")
        print("\n")


def rotate(matrix,link,m):
    n=m
    c=0
    while(n>1):
        for i in range(n-1):
            t=matrix[c][c+i]
            link[c][c+i]=[link[c][c+i][1],(m-link[c][c+i][0]-1)]

            matrix[c][c+i]=matrix[m-c-1 -i][c]
            link[m-c-1 -i][c]=[link[m-c-1 -i][c][1],(m-link[m-c-1 -i][c][0]-1)]

            matrix[m-c-1 -i][c]=matrix[m-c-1][m-c-1 -i]
            link[m-c-1][m-c-1 -i]=[link[m-c-1][m-c-1 -i][1],(m-link[m-c-1][m-c-1 -i][0]-1)]

            matrix[m-c-1][m-c-1 -i]=matrix[c+i][m-c-1]
            link[c+i][m-c-1]=[link[c+i][m-c-1][1],(m-link[c+i][m-c-1][0]-1)]

            matrix[c+i][m-c-1]=t
        c=c+1 
        n=n-2

    disp(matrix,m)
    disp(link,m)







link=[]
matrix=[]
n=int(input())
for i in range(n):
    temp=list(map(int,input().split() ))
    matrix.append(temp)

for i in range(n):
    temp1=[]
    for j in range(n):
        temp=[i,j]
        temp1.append(temp)
    link.append(temp1)


while True:
    s=input()
    if(s=="-1"):
        break
    elif(s[0]=="A"):
        loop=int(s[2:])//90
        loop=loop%4
        for i in range(loop):
            rotate(matrix,link,n)

    elif(s[0]=="Q"):
        s=list(map(int,s.split()[1:] ))
        print(matrix[ s[0]-1 ][ s[1]-1 ])

    elif(s[0]=="U"):
        s=list(map(int,s.split()[1:] ))
        pos=link[ s[0]-1 ][ s[1]-1 ]
        matrix[ pos[0] ][ pos[1] ]=s[2]
        disp(matrix,n)
        disp(link,n)


"""
5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
A 90
A 270
A 270
U 5 5 721
A 360
A 360
Q 1 1
-1
"""