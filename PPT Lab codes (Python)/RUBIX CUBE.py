"""
SudoKube
Problem Description
John, a research scholar / Professor / Puzzle solver wants your help in publishing his work on SudoKube on his online blog for his followers and students.
A SudoKube is a mixture of Rubics cube and Sudoku. A SudoKube has exactly 6 appearances of every digit from 1 to 9 across the cube, whereas Rubics cube has 6 different colours.
As John wants to publish his work in text /document form (no video) he's concerned how he would depict the step by step work of rotation in 2D form. Following are the notions and concepts John follows:
1. The six faces of the cube are named FRONT, BACK, UP, DOWN, LEFT and RIGHT respectively.
2. Just like a Rubics cube which move in 90 and 180 degrees in both clockwise and anti clockwise directions, so can the SudoKube
3. Any given face of the cube is a 3x3 square matrix whose indices are denoted by (0,0) to (2,2). Diagram below illustrates the same.
4. An elementary move is denoted in the following fashion.
i. If a given face is rotated by 90 degrees clockwise about the axis passing from the centre of the face to the centre of the cube, the move is denoted by the first letter of the name of the face.
ii. If the rotation is anticlockwise by 90 degrees, the letter is followed by an apostrophe (').
iii. If the rotation is by 180 degrees, the letter is followed by a 2.
 
Above image display the position of the faces
 
Above diagram displays the indices of the matrix on the faces
John wants to test his notations on you. He has given you the initial position of the SudoKube and he has given you a set of operations to be performed on the SudoKube basis his notation. After applying all the operations, the final SudoKube state should be the same as what John expects. Your task is to apply the operations and print the final SudoKube state.
Constraints
Values in SudoKube will be between 1 and 9
No of moves < 15
Input
• First eighteen lines contain the values of the faces on SudoKube in the order given below
D D D
D D D
D D D
U U U
U U U
U U U
L L L
L L L
L L L
F F F
F F F
F F F
R R R
R R R
R R R
B B B
B B B
B B B
where
o	D for Down face
o	U for upper face
o	L for Left face
o	F for Front face
o	R for Right face
o	B for Back face.
Input contains digits from 1 to 9 instead of letters; letters are displayed for better understanding of the faces and the expected input format
• Nineteenth line contains a sequence of space delimited moves that need to be performed on the SudoKube
Example 1: D F2 R' U - to understand this please refer second example from the Examples section below
Example 2: L2 U B F' D2 R - lets understand how to interpret this set of operations
o	L2 means rotate the Left side by 180 degrees
o	U means rotate the Up side by 90 degrees clockwise
o	B means rotate the Back side by 90 degrees clockwise
o	F' means rotate the Front side by 90 degrees anticlockwise
o	D2 means rotate the Down side by 180 degrees
o	R means rotate the Right side by 90 degrees clockwise
In summary, first eighteen lines denotes the state of the SudoKube, 19th line denotes the operation to be performed on that state and output should be the resulting state.
Output
Print 3x3 matrix corresponding to the order (D, U, L, F, R, B). Between every 3x3 matrix there should be a new line.
Time Limit
1
Examples
Example 1
Input
4 7 1
2 8 7
6 3 5
5 8 3
3 1 6
9 4 2
5 2 4
3 7 8
5 1 9
6 1 4
9 4 8
2 5 7
7 9 1
1 9 6
6 2 8
8 6 3
7 2 5
3 9 4
F
Output
6 1 7
2 8 7
6 3 5
 
5 8 3
3 1 6
9 8 4
 
5 2 4
3 7 7
5 1 1
 
2 9 6
5 4 1
7 8 4
 
9 9 1
4 9 6
2 2 8
 
8 6 3
7 2 5
3 9 4
Explanation:
The output shows the state of SudoKube when the front side is rotated clockwise
Example 2
Input
4 7 1
2 8 7
6 3 5
5 8 3
3 1 6
9 4 2
5 2 4
3 7 8
5 1 9
6 1 4
9 4 8
2 5 7
7 9 1
1 9 6
6 2 8
8 6 3
7 2 5
3 9 4
D F2 R' U
Output
2 4 5
3 8 9
5 7 6
 
4 3 5
2 1 8
8 7 6
 
9 1 3
3 7 1
3 9 7
 
1 6 7
8 4 6
4 1 6
 
1 6 3
9 9 5
4 8 4
 
5 2 2
7 2 5
9 2 8

Explanation
The above output prints the state of cube after D F2 R' U operation are performed. Here
· D means rotate the Down side by 90 degrees clockwise
· F2 means rotate the Front side by 180 degrees
· R' means rotate the Right side by 90 degrees anti clockwise
· U means rotate the Up side by 90 degrees clockwise


Example 3
Input
4 7 1
2 8 7
6 3 5
5 8 3
3 1 6
9 4 2
5 2 4
3 7 8
5 1 9
6 1 4
9 4 8
2 5 7
7 9 1
1 9 6
6 2 8
8 6 3
7 2 5
3 9 4
L2 F2 B2 D2 U2 L2 R2 R2 B2 F2 B2 U2 D2 R2

Output
2 4 3
3 8 7
6 3 4

5 8 9
2 1 6
1 7 5

5 1 6
1 7 3
5 2 7

7 5 3
5 4 9
4 1 8

8 9 4
8 9 6
1 2 9

6 6 3
7 2 8
2 9 4



"""



def disp(up,down,left,front,right,back):
    print("\n")
    for i in range(3):
        for j in range(3):
            print(" ",end=" ")
        print(" ",end="")
        for j in range(3):
            print(up[i][j],end=" ")
        print()
    print()


    for i in range(3):
        for j in range(3):
            print(left[i][j],end=" ")
        print(" ",end="")
        
        for j in range(3):
            print(front[i][j],end=" ")
        print(" ",end="")
        
        for j in range(3):
            print(right[i][j],end=" ")
        print(" ",end="")

        for j in range(3):
            print(back[i][j],end=" ")
        print(" ",end="")
        print()
    print()

    for i in range(3):
        for j in range(3):
            print(" ",end=" ")
        print(" ",end="")
        for j in range(3):
            print(down[i][j],end=" ")
        print()

    print("\n")

def dspv2(up,down,left,front,right,back):
    print("\n")
    for i in range(3):
        for j in range(3):
            print(down[i][j],end=" ")
        print()
    print()

    for i in range(3):
        for j in range(3):
            print(up[i][j],end=" ")
        print()
    print()

    for i in range(3):
        for j in range(3):
            print(left[i][j],end=" ")
        print()
    print()

    for i in range(3):
        for j in range(3):
            print(front[i][j],end=" ")
        print()
    print()

    for i in range(3):
        for j in range(3):
            print(right[i][j],end=" ")
        print()
    print()

    for i in range(3):
        for j in range(3):
            print(back[i][j],end=" ")
        print()
    print()


def x1(up,down,left,front,right,back):
    
    for i in range(3):
        t=front[i][0]
        front[i][0]=down[i][0]
        down[i][0]=back[3-i-1][2]
        back[3-i-1][2]=up[i][0]
        up[i][0]=t
    for i in range(2):
        t=left[0][i]
        left[0][i]=left[i][2]
        left[i][2]=left[2][3-i-1]
        left[2][3-i-1]=left[3-i-1][0]
        left[3-i-1][0]=t
    disp(up,down,left,front,right,back)

def x1r(up,down,left,front,right,back):
    
    for i in range(3):
        t=up[i][0]
        up[i][0]=back[3-i-1][2]
        back[3-i-1][2]=down[i][0]
        down[i][0]=front[i][0]
        front[i][0]=t

    for i in range(2):
        t=left[3-i-1][0]
        left[3-i-1][0]=left[2][3-i-1]
        left[2][3-i-1]=left[i][2]
        left[i][2]=left[0][i]
        left[0][i]=t
    disp(up,down,left,front,right,back)

def x2(up,down,left,front,right,back):
    
    for i in range(3):
        t=front[i][1]
        front[i][1]=down[i][1]
        down[i][1]=back[3-i-1][1]
        back[3-i-1][1]=up[i][1]
        up[i][1]=t
    disp(up,down,left,front,right,back)
def x2r(up,down,left,front,right,back):
    
    for i in range(3):
        t=up[i][1]
        up[i][1]=back[3-i-1][1]
        back[3-i-1][1]=down[i][1]
        down[i][1]=front[i][1]
        front[i][1]=t
    disp(up,down,left,front,right,back)

def x3(up,down,left,front,right,back):
    
    for i in range(3):
        t=front[i][2]
        front[i][2]=down[i][2]
        down[i][2]=back[3-i-1][0]
        back[3-i-1][0]=up[i][2]
        up[i][2]=t
        
    for i in range(2):
        t=right[3-i-1][0]
        right[3-i-1][0]=right[2][3-i-1]
        right[2][3-i-1]=right[i][2]
        right[i][2]=right[0][i]
        right[0][i]=t
    disp(up,down,left,front,right,back)

def x3r(up,down,left,front,right,back):
    
    for i in range(3):
        t=up[i][2]
        up[i][2]=back[3-i-1][0]
        back[3-i-1][0]=down[i][2]
        down[i][2]=front[i][2]
        front[i][2]=t

    for i in range(2):
        t=right[0][i]
        right[0][i]=right[i][2]
        right[i][2]=right[2][3-i-1]
        right[2][3-i-1]=right[3-i-1][0]
        right[3-i-1][0]=t
    disp(up,down,left,front,right,back)


def y1(up,down,left,front,right,back):
    
    for i in range(3):
        t=left[2][i]
        left[2][i]=back[2][i]
        back[2][i]=right[2][i]
        right[2][i]=front[2][i]
        front[2][i]=t
        
        
    for i in range(2):
        t=down[3-i-1][0]
        down[3-i-1][0]=down[2][3-i-1]
        down[2][3-i-1]=down[i][2]
        down[i][2]=down[0][i]
        down[0][i]=t
    disp(up,down,left,front,right,back)


def y1r(up,down,left,front,right,back):
    for i in range(3):
        t=front[2][i]
        front[2][i]=right[2][i]
        right[2][i]=back[2][i]
        back[2][i]=left[2][i]
        left[2][i]=t

    for i in range(2):
        t=down[0][i]
        down[0][i]=down[i][2]
        down[i][2]=down[2][3-i-1]
        down[2][3-i-1]=down[3-i-1][0]
        down[3-i-1][0]=t
    disp(up,down,left,front,right,back)
        
        

def y2(up,down,left,front,right,back):
    
    for i in range(3):
        t=left[1][i]
        left[1][i]=back[1][i]
        back[1][i]=right[1][i]
        right[1][i]=front[1][i]
        front[1][i]=t
    disp(up,down,left,front,right,back)


def y2r(up,down,left,front,right,back):
    for i in range(3):
        t=front[1][i]
        front[1][i]=right[1][i]
        right[1][i]=back[1][i]
        back[1][i]=left[1][i]
        left[1][i]=t
    disp()

def y3(up,down,left,front,right,back):
    
    for i in range(3):
        t=left[0][i]
        left[0][i]=back[0][i]
        back[0][i]=right[0][i]
        right[0][i]=front[0][i]
        front[0][i]=t

    for i in range(2):
        t=up[0][i]
        up[0][i]=up[i][2]
        up[i][2]=up[2][3-i-1]
        up[2][3-i-1]=up[3-i-1][0]
        up[3-i-1][0]=t
    disp(up,down,left,front,right,back)

def y3r(up,down,left,front,right,back):
    for i in range(3):
        t=front[0][i]
        front[0][i]=right[0][i]
        right[0][i]=back[0][i]
        back[0][i]=left[0][i]
        left[0][i]=t
        
    for i in range(2):
        t=up[3-i-1][0]
        up[3-i-1][0]=up[2][3-i-1]
        up[2][3-i-1]=up[i][2]
        up[i][2]=up[0][i]
        up[0][i]=t
    disp(up,down,left,front,right,back)


def z1(up,down,left,front,right,back):
    
    for i in range(3):
        t=up[0][i]
        up[0][i]=left[3-i-1][0]
        left[3-i-1][0]=down[2][3-i-1]
        down[2][3-i-1]=right[i][2]
        right[i][2]=t

    for i in range(2):
        t=back[0][i]
        back[0][i]=back[i][2]
        back[i][2]=back[2][3-i-1]
        back[2][3-i-1]=back[3-i-1][0]
        back[3-i-1][0]=t
    disp(up,down,left,front,right,back)

def z1r(up,down,left,front,right,back):
    for i in range(3):
        t=right[i][2]
        right[i][2]=down[2][3-i-1]
        down[2][3-i-1]=left[3-i-1][0]
        left[3-i-1][0]=up[0][i]
        up[0][i]=t
        
    for i in range(2):
        t=back[3-i-1][0]
        back[3-i-1][0]=back[2][3-i-1]
        back[2][3-i-1]=back[i][2]
        back[i][2]=back[0][i]
        back[0][i]=t
    disp(up,down,left,front,right,back)

def z2(up,down,left,front,right,back):
    for i in range(3):
        t=up[1][i]
        up[1][i]=left[3-i-1][1]
        left[3-i-1][1]=down[1][3-i-1]
        down[1][3-i-1]=right[i][1]
        right[i][1]=t
    disp(up,down,left,front,right,back)

def z2r(up,down,left,front,right,back):
    for i in range(3):
        t=right[i][1]
        right[i][1]=down[1][3-i-1]
        down[1][3-i-1]=left[3-i-1][1]
        left[3-i-1][1]=up[1][i]
        up[1][i]=t
    disp(up,down,left,front,right,back)

def z3(up,down,left,front,right,back):
    
    for i in range(3):
        t=up[2][i]
        up[2][i]=left[3-i-1][2]
        left[3-i-1][2]=down[0][3-i-1]
        down[0][3-i-1]=right[i][0]
        right[i][0]=t
    
    for i in range(2):
        t=front[0][i]
        front[0][i]=front[3-i-1][0]
        front[3-i-1][0]=front[2][3-i-1]
        front[2][3-i-1]=front[i][2]
        front[i][2]=t
    disp(up,down,left,front,right,back)

def z3r(up,down,left,front,right,back):
    for i in range(3):
        t=right[i][0]
        right[i][0]=down[0][3-i-1]
        down[0][3-i-1]=left[3-i-1][2]
        left[3-i-1][2]=up[2][i]
        up[2][i]=t
        
    for i in range(2):

        t=front[i][2]
        front[i][2]=front[2][3-i-1]
        front[2][3-i-1]=front[3-i-1][0]
        front[3-i-1][0]=front[0][i]
        front[0][i]=t
    disp(up,down,left,front,right,back)
        

        







def choosePreset(up,down,left,front,right,back):

    defpreset={    
                "front":[ 
                        ["B","B","B"],
                        ["B","B","B"],
                        ["B","B","B"]
                    ],
                "back":[  
                        ["G","G","G"],
                        ["G","G","G"],
                        ["G","G","G"]
                    ],
                "left":[  
                        ["O","O","O"],
                        ["O","O","O"],
                        ["O","O","O"]
                    ],
                "right":[ 
                        ["R","R","R"],
                        ["R","R","R"],
                        ["R","R","R"]
                    ],
                "up":[    
                        ["Y","Y","Y"],
                        ["Y","Y","Y"],
                        ["Y","Y","Y"]
                    ],
                "down":[  
                        ["W","W","W"],
                        ["W","W","W"],
                        ["W","W","W"]
                    ]
            }



    
    while True:
        choice=input("custom preset or default preset of cube?\npress C for custom preset\npress D for default preset\nchoose: ")
        if choice=='D' or choice=='d':
            front=defpreset["front"]
            back=defpreset["back"]
            left=defpreset["left"]
            right=defpreset["right"]
            up=defpreset["up"]
            down=defpreset["down"]
            break

        elif choice=='C' or choice=='c':
            up,down,left,front,right,back=[],[],[],[],[],[]
            print(  "always postion centres of faces as follow\n&\nonly use uppercase abrivietion of the color:\n" 
                    "up-Yellow(Y)\n"
                    "down-White(W)\n"
                    "left-Orange(O)\n"
                    "front-Blue(B)\n"
                    "right-Red(R)\n"
                    "back-Green(G)\n"
                )
            for i in range(3):
                temp=input().split()[0:3]
                up.append(temp)

            for i in range(3):
                temp=input().split()[0:3]
                down.append(temp)

            for i in range(3):
                temp=input().split()[0:3]
                left.append(temp)

            for i in range(3):
                temp=input().split()[0:3]
                front.append(temp)

            for i in range(3):
                temp=input().split()[0:3]
                right.append(temp)

            for i in range(3):
                temp=input().split()[0:3]
                back.append(temp)
            break


    return up,down,left,front,right,back







def checkMove(up,down,left,front,right,back,move):

    if len(move)==2:
            
        if move=="L'" or move=="l'":
            x1(up,down,left,front,right,back)
        elif move=="R'"  or move=="r'":
            x3r(up,down,left,front,right,back)
        elif move=="D'" or move=="d'":
            y1r(up,down,left,front,right,back)
        elif move=="U'" or move=="u'":
            y3(up,down,left,front,right,back)
        elif move=="B'" or move=="b'":
            z1(up,down,left,front,right,back)
        elif move=="F'" or move=="f'":
            z3r(up,down,left,front,right,back)
        

    else:
        if move=="L" or move=="l":
            x1r(up,down,left,front,right,back)
        elif move=="R" or move=="r":
            x3(up,down,left,front,right,back)
        elif move=="D" or move=="d":
            y1(up,down,left,front,right,back)
        elif move=="U" or move=="u":
            y3r(up,down,left,front,right,back)
        elif move=="B" or move=="b":
            z1r(up,down,left,front,right,back)
        elif move=="F" or move=="f":
            z3(up,down,left,front,right,back)

 









#IN PROGRESS
def autoFix(up,down,left,front,right,back):


    # while not(down[0][1]=="W" and down[1][0]=="W" and down[1][2]=="W" and down[2][1]=="W" and front[2][1]=="B" and  back[2][1]=="G" and left[2][1]=="O" and right[2][1]=="R") :
    #     moves=[]
    #     for move in moves:    
    #         checkMove(up,down,left,front,right,back,move)








    while not(front[2][2]=="B" and right[2][0]=="R" and down[0][2]=="W") :
        moves=["r","u","r'","u'"]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)

    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)


    while not(front[2][2]=="O" and right[2][0]=="B" and down[0][2]=="W") :
        moves=["r","u","r'","u'"]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)

    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)

    while not(front[2][2]=="G" and right[2][0]=="O" and down[0][2]=="W") :
        moves=["r","u","r'","u'"]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)

    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)


    while not(front[2][2]=="R" and right[2][0]=="G" and down[0][2]=="W") :
        moves=["r","u","r'","u'"]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)

    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)





    while not(front[1][2]=="B" and right[1][0]=="R") :
        moves=["u","r","u","r'","u'" ]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)

    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)

    while not(front[1][2]=="O" and right[1][0]=="B") :
        moves=["u","r","u","r'","u'" ]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)
    
    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)

    while not(front[1][2]=="G" and right[1][0]=="O") :
        moves=["u","r","u","r'","u'" ]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)
    
    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)

    while not(front[1][2]=="R" and right[1][0]=="G") :
        moves=["u","r","u","r'","u'" ]
        for move in moves:    
            checkMove(up,down,left,front,right,back,move)
    
    y1(up,down,left,front,right,back)
    y2(up,down,left,front,right,back)
    y3(up,down,left,front,right,back)



    return up,down,left,front,right,back






def humanPlay(up,down,left,front,right,back):

    disp(up,down,left,front,right,back)
    while True:
        
        move=input("enter move: ")    
        if move=="E" or move=="e" :
            break
        else:
            checkMove(up,down,left,front,right,back,move)
    return up,down,left,front,right,back






def main():
    front=[]
    back=[]
    left=[]
    right=[]
    up=[]
    down=[]

    up,down,left,front,right,back=choosePreset(up,down,left,front,right,back)

    while True:
        choice=input("press A for Auto Fix a cube\npress B for play the cube by yourself\npress C to choose preset\npress E to exit\nchoose: ")
        
        if choice=='A' or choice=='a':
            up,down,left,front,right,back=autoFix(up,down,left,front,right,back)
        elif choice=='B' or choice=='b':
            up,down,left,front,right,back=humanPlay(up,down,left,front,right,back)
        elif  choice=='C' or choice=='c':
            up,down,left,front,right,back=choosePreset(up,down,left,front,right,back)
        elif choice=='E' or choice=='e':
            break


if __name__ == "__main__":
    main()


"""
all possible moves:
F F2 F'

B B2 B'

U U2 U'

D D2 D'

L L2 L'

R R2 R'

asked moves and corresponding function:
X1= L'
X1R=L

X3=R
X3R=R'


Y1=D
Y1R=D'

Y3=U'
Y3R=U


Z1=B'
Z1R=B

Z3=F
Z3R=F'

"""

