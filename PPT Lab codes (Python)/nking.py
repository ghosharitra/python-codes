def check(r1,c1,chessboard,r,c):
  for i in range(r1-1,r1+2):
    for j in range(c1-1,c1+2):
      if (0<=i and i<r) and (0<=j and j<c):
        if chessboard[i][j]==1:
          return True
  return False

def nking(i,j, chessboard,sum):
  r=len(chessboard)
  c=len(chessboard[0])
  
  if count(chessboard)==r*c:
    return sum
  else:
    chessboard[i][j]
  
  
  
  
  
  
  



r=list(map(int,input().split()))
c=r[1]
r=r[0]

chessboard=[]

for i in range(r):
  temp=[]
  for j in range(c):
    temp.append(0)
  chessboard.append(temp)

print(chessboard)
list=[]
for i in range(r):
  for j in range(c):
    l.append(nking(i,j,chessboard,0))

print("max no. of king",max(l))




