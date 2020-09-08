"""
ARRAY Q11)
Given n doors and n persons. 
The doors are numbered from 1 to n and 
persons are given id’s numbered from 1 to n. 
Each door can have only two statuses ie open (1) or 
closed (0) . Initially all the doors have status closed. 
Find the final status of all the doors, 
when all the persons have changed the status of 
the doors of which they are authorized. i.e. if status 
open then change the status to closed and vice versa. 
A person with id ‘i’ is authorized to change the status 
of door numbered ‘j’ if ‘j’ is a multiple of ‘i’.

Note: A person has to change the current status of all 
the doors for which he is authorized exactly once.

Example:
Input : 3
Output : 1 0 0

Explanation : Initially status of rooms 0 0 0 person with 
id 2 changes room 2 to open ie (0 1 0) person with id 1 
changes room 1, 2, 3 status (1 0 1) person with id 3 
changes room 3 status ie (1 0 0)


Input:
The first line of input contains an integer T denoting 
the no of test cases. Then T test cases follow. 
Each test case contains an integer n.

Output:
For each test case in a new line print the n space 
separated integers  either (1 or 0) depending on the 
status of the ith door where 1 denotes the door is 
open and a 0 denotes door is closed.

Constraints:
1 <= T <= 100
1 <= N <= 1000

Example:
Input:
2
3
5
Output:
1 0 0                    
1 0 0 1 0                                   

"""



import math 

l=0
res=""
for _ in range(int(input())):
    n=int(input())
    if(l<n):
        for i in range(l+1,n+1):
            l+=1
            tmp=int(math.sqrt(i))
            if(tmp*tmp==i):
                res=res+"1"
            else:
                res=res+"0"
    print(res[:n])

