"""
A man is doing an something experiment with the device that he built newly. The structure of the device is shown  as below diagram.B to E is a sloping surface with n holes, labelled H1, H2,H3 ... Hn, on it. Holes are of different diameters & depths. The man is releasing m no.of balls of different diameters from the point B one after the other.
 He wants to ﬁnd the positions of each ball after the experiment.  The specialties of the device are as follow:
 
1. A ball will fall into a hole, if and only if its diameter is less than or equal to the diameter of the hole.
 
2. A hole Hi will become Non empty i.e Full, if i no. of balls fall into it. For ex hole labelled as H3 will become full if THREE balls fall into it.
 
3. If a hole is full then no more balls can fall into that hole . 
 
4. A ball will reach the bottom point E from B, only if it is not falling into any 1 of the holes.
 
Please help him in ﬁnding the eventual position of the balls. If a ball is in hole Pi, then take its position as i. If a ball reached the bottom point E, then take its position as 0. 
 
 Constraints
0 < N <= 50
0 < Diameter of holes <= 10^9
0 < M <= 1000
0 < M <= 1000
Input Format
Line 1: total number of holes, N
Line 2: N space separated integers denoting the diameters of N holes, from bottom to top
Line 3: total number of balls, M 
Line 4: M space separated integers denoting the diameters of balls in the order of release. 
Output 
Line 1: Positions of each ball in the order of ball release separated by space 

Explanation 
Input
3
21 3 6 
11 
20 15 5 7 10 4 2 1 3 6 8

 
Output
1 0 3 0 0 3 3 2 2 0 0

Explanation
3 holes are there labelled H1, H2, and H3 of diameters 21, 3, and 6 respectively. 11 balls are released from the point B in the order provided in the input i.e. { 20, 15, 5, 7 ..., 5}.
 
Ball of diameter 20 will fall into the hole H1 and the hole H1 will become full. Balls 15, 7 and 10 will reach bottom since hole H1 is full and diameters of holes H2 and H3 are less than balls diameter. Balls 5, 4 , and 2 will fall into the hole H3. Ball 1 will fall into the hole H2 since the hole H3 is already full. Ball 3 will fall into hole H2. Balls 6, and 8 will reach at the bottom point E. The position of ball 20 is 1 because it is in hole H1. Positions of ball 15, 7, 10, 3, 6, and 8 are 0 because they reached bottom point E. Positions of 5, 4, and 2 are 3 because they are in hole H3. Position of Ball 1 and Ball 3 is 2. 

"""
def sol(noOfBalls,balls,noOfHoles,holes):

    res=[0]*(noOfBalls)
    filled=[0]*noOfHoles

    for i in range(noOfBalls):

        for j in range(noOfHoles-1,-1,-1):
            #print("i=",i,"j=",j,"balls[i]=",balls[i],"holes[j]=",holes[j],"filled[j]=",filled[j])
            if(holes[j]>=balls[i] and filled[j]<j+1 ):
                filled[j]+=1
                res[i]=j+1
                break
        else:
            res[i]=0


    return res

try:
    noOfHoles=int(input())
    holes=list(map(int,input().split() ))

    if len(holes)!=noOfHoles:
        raise Exception
    
    noOfBalls=int(input())
    balls=list(map(int,input().split() ))

    if len(balls)!=noOfBalls:
        raise Exception
except:
    print("Invalid Input")

res=sol(noOfBalls,balls,noOfHoles,holes)
for i in res:
    print(i,end=" ")