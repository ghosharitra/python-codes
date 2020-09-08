"""
Welcome to the world Zandar, the second most outstanding planet within the Milky Way Galaxy (of course after our own Earth). The world is in a very distress condition, a gaggle of Galactic pirates, Zorons have purloined the shaft Crystal, that is that the main supply of energy of the world, and square measure escaping the Galaxy. The star Corps, the military agency of Zandar, have gathered intelligence that the Zoronion house craft will run in cosmic leaps of specifically D units,  (it means that the space craft have to move D units or steps from its position in every leap/turn) & is currently I units away from Zandar. 

The Zandarian crafts can run in cosmic leaps of precisely or exactly Z units. The Commander of Nova Corps wants to know the smallest no. of leaps needed to catch Zorons

 Note  :  It is possible to catch the pirates only when they will be at the same point in the cosmic universe. 

Zorons despite the fact that area unit clever thieves , travel in 1 direction, as well as keep jumping precisely or exactly D units without stopping at possibly any point. The Nova Corps can dial in the no. of jumps they need to make (each of them  precisely or exactly Z units), & reach the place almost instantly. They can then wait there till the Zorons arrive, & recover the Trident Crystal. 

However, their wizard has told them that is also things wherever it's not possible  for the Nova corps to be at the an equivalent distance as the Zorons. 

As the planet is out of power currently, their supercomputers are shut down & they unable to determine or calculate the required information. As you are there from Earth they have approached you for help.

Note: one dimensional Cosmic universe .
Input Format
An integer T for no. of test cases, followed by T test cases each 1 consisting of 3 numbers 
1) I :- Zorons's initial distance 
2) D:- distance covered leap by Zoronion space craft. 
3) Z:- Zandarian space crafts's covered distance .
Output Format
Single number, the no. of leaps required to catch the pirates, & if it is impossible to catch them, print -1
Constraints
 1 ≤ I,D ≤ 1012 1≤ Z ≤ 109
Sample Input and Output 
Example 1

Input
2 
9 5 12
5 7 9
Output
2 6

Explanation
In the 1st test case, The Zorons will initially be at 9 & then they will leap to 14,19 24.....  The Nova Corps can take leaps of 12 & will catch them nearest at a distance 24, taking 2 leaps 12 & 24.
In the 2nd test case, The Zorons will initially be at 5 & then they will leap to 12,19 26, 33, 40, 47, 54.....  The Nova Corps can take leaps of 9 & will catch them nearest at 54, taking 6 leaps.
Therefore the o/p has 2 lines, 2 and 6.

Example 2

Input
1 
10 15 20
Output
2

Explanation
The Zorons will initially be at 10, & jump in jumps of 15, landing at 25,40 
The Nova Corps take leaps of 20, & arrive at 20, 40. 
Therefore, they can meet at 40 after 2 leaps. The o/p is 2.

Note:
The solution is so simple but it seems little complicated because of the condition: If it is impossible to catch return -1.

"""
import math

def sol(info):
    if info[0] % math.gcd(info[1],info[2]) != 0:
        print("-1")
        exit(0)
    i=0
    while True:
        if(info[0]+info[1]*i)%info[2]==0:
            return (info[0]+info[1]*i)//info[2]
        i=i+1
try:
    t=int(input())
    info=[]
    for i in range(t):
        temp=list(map(int,input().split()))
        if len(temp)!=3:
            raise Exception
        info.append(temp)
except:
    print("Invalid Exception")

for i in range(t):
    res=sol(info[i])
    print(res,end=" ")
