def display(a,n):
  for i in range(n):
    for j in range(n):
      print(a[i][j],end=" ")
    print()
  

 



n,k=map(int,input("enter size of board and no. of obstacles: ").split())
qx,qy=map(int,input("enter queen location: ").split())
qx=qx-1
qy=qy-1
oloc=[]
for i in range(k):
  oloc.append(list(map(lambda x: int(x)-1,input("enter obsacle location: ").split())))
 




board=[]

for i in range(n):
  temp=[]
  for j in range(n):
    if qx==i and qy==j:
      temp.append('Q')
    else:
      temp.append('X')
  board.append(temp)

for i in oloc:
  board[i[0]][i[1]]='O'


display(board,n)

qmoves=0
i,j=qx+1,qy+1
while i<n and j<n:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  i+=1
  j+=1
  

i,j=qx-1,qy-1
while i>=0 and j>=0:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  i-=1
  j-=1


i,j=qx-1,qy+1
while i>=0 and j<n:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  i-=1
  j+=1


i,j=qx+1,qy-1
while i<n and j>=0:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  i+=1
  j-=1


i,j=qx+1,qy
while i<n:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  i+=1


i,j=qx-1,qy
while i>=0:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  i-=1

 
i,j=qx,qy+1
while j<n:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  j+=1


i,j=qx,qy-1
while j>=0:
  if board[i][j]!='O':
    print(i,j)
    qmoves+=1
  else:
    break
  j-=1
 
 
print("no. of possible moves:",qmoves)
     