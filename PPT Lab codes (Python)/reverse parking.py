"""
A futuristic company is building an autonomous car. The scientists at the company are training the car to perform Reverse parking. To park, the car needs to be able to move in backward as well as forward direction. The car is programmed to move backwards B meters and forwards again, say F meters, in a straight line. The car does this repeatedly until it is able to park or collides with other objects. The car covers 1 meter in T units of time. There is a wall after distance D from car's initial position in the backward direction.

The car is currently not without defects and hence often hits the wall. The scientists are devising a strategy to prevent this from happening. Your task is to help the scientists by providing them with exact information on amount of time available before the car hits the wall.

Input Format

First line contains total number of test cases, denoted by N
Next N lines, contain a tuple containing 4 values delimited by space F B T D, where
1. F denotes forward displacement in meters
2. B denotes backward displacement in meters
3. T denotes time taken to cover 1 meter
4. D denotes distance from Car's starting position and the wall in backward direction

Constraints

First move will always be in backward direction
1 <= N <= 100
backward displacement > forward displacement i.e. (B > F)
forward displacement (F) > 0
backward displacement (B) > 0
time (T) > 0
distance (D) > 0
All input values must be positive integers only

Output Format

For each test case print time taken by the Car to hit the wall.


i/p:
2
6 2 4 15 
5 1 4 12                                                                                     
o/p:
-84
-72


i/p:
1
4 2 8 6
o/p:
-144



i/p:
2
6 9 3 18
3 7 5 20
o/p:
162
220

"""



def sol(target):

    res=0

    f=target[0]
    b=target[1]
    t=target[2]
    d=target[3]

    pos=d
    while(pos>0):
        print("pos:",pos,end=" ")
        if(b>=pos):
            res=res+pos
            print("res",res)
            break
        elif(b<pos):
            pos=pos-b
            pos=pos+f
            res=res+b+f
            print("res",res)



    return res*t

def sol1(target):

    
    res=0

    f=target[0]
    b=target[1]
    t=target[2]
    d=target[3]

    if((d-b)%(d-f)==0):
        print()
        res=(((d-b)/(d-f))*(d+f) +b )*t
    else:
        val=((d-b)//(b-f) + 1)
        res = ( val*(d+f)+ (d-(val*(d-f))) )*t
    print("res=",res)





target=[]
try:
    t=int(input())
    if (t<=0 or t>100):
        raise Exception()
        exit(0)
    for i in range(t):
        target.append(list(map(int,input().split())))
        if(target[i][1]<=target[i][0] or target[i][0]<=0 or target[i][1]<=0 or target[i][2]<=0 or target[i][3]<=0):
            raise Exception()
except:
    print("-1")
    exit(0)

for i in range(t):
    res=sol(target[i])
    print(res)
    sol1(target[i])