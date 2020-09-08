"""
The task is to count all the possible paths from top left to bottom right of a m x n matrix with the constraints that from each cell you can either move only to right or down.

Input: 

First line consists of T test cases. First line of every test case consists of N and M, denoting the number of rows and number of columns respectively.
Output: 

Single line output i.e count of all the possible paths from top left to bottom right of a m x n matrix..
Constraints:

1<=T<=100
1<=N<=100
1<=M<=100

"""


def sol(r,c):
    print("matrix:",matrix)
    if(matrix[r][c]!=0):
        return matrix[r][c]

    if(r==0 or  c==0):
        matrix[r][c]=1
        return matrix[r][c]
    
    res=sol(r,c-1) + sol(r-1,c)
    matrix[r][c]=res
    return matrix[r][c]


try:
    t=int(input())
    info=[]
    for i in range(t):
        temp=list(map(int,input().split() ))
        info.append(temp)
except:
    print("Invalid Input")
    exit(0)


for i in range(t):
    matrix=[]
    for j in range(info[i][0]):
        temp=[0]*info[i][1]
        matrix.append(temp)
    res=sol(info[i][0]-1,info[i][1]-1)
    print("matrix:",matrix)
    print(res)
