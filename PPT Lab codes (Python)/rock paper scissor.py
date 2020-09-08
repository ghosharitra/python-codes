"""
STRINGS Q9)
The RPS world championship is here. 
Here two players A and B play the game. 
You need to determine who wins.
Both players can choose moves from the set {R,P,S}.
The game is a draw if both players choose the same item.
The winning rules of RPS are given below:

Rock crushes scissor
Scissor cuts paper
Paper envelops rock

Input:
The first line of input contains T denoting 
the number of testcases. 
T testcases follow. 
Each testcase contains single line of input 
that contains two characters sidebyside. 
These characters denote the moves of players A and B 
respectively.

Output:
For each testcase, in a newline, print the winner. 
If match is draw, print 'DRAW'.

Constraints:
1<= T <= 50

Example:
Input:
7
RR
RS
SR
SP
PP
PS
RP
Output:
DRAW
A
B
A
DRAW
B
B

"""


for _ in range(int(input())):
    move=input()
    if move[0]=="R":
        if move[1]=="S":
            print("A")
        elif move[1]=="P":
            print("B")
        else:
            print("DRAW")

    
    elif move[0]=="P":
        if move[1]=="R":
            print("A")
        elif move[1]=="S":
            print("B")
        else:
            print("DRAW")
    
    elif move[0]=="S":
        if move[1]=="P":
            print("A")
        elif move[1]=="R":
            print("B")
        else:
            print("DRAW")