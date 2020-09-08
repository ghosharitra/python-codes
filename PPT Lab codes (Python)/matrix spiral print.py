matrix=[]
r,c=map(int,input().split())
s=list(map(int,input().split()))
if r<=2 or r>=10 or c<=2 or c>=10:
    print(-1)
else:    
    n=r*c
    
    for i in range(r):
        matrix.append(  s[(i*c):(i*c + c)]  )

    #print(matrix)

    count=0
    i=0
    while(True):

        for j in range(i,c-i):
            count=count+1
            print(matrix[i][j],end=" ")

        if(count>=n):
            break
        
        for j in range(i+1,r-i-1):
            count=count+1
            print(matrix[j][c-i-1],end=" ")

        if(count>=n):
            break

        for j in range(c-i-1,i-1,-1):
            count=count+1
            print(matrix[r-i-1][j],end=" ")
        
        if(count>=n):
            break

        for j in range(r-i-2,i,-1):
            count=count+1
            print(matrix[j][i],end=" ")

        if(count>=n):
            break

        i=i+1

        
        