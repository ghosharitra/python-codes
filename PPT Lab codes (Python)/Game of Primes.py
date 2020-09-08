"""
In a world wide Mathematics contest, the Mathematics  contestants are told to invent some very unique and special numbers which can be created by adding the squares of its digits. 
Doing this enduring, the numbers will end up to 1 or 4.
If a positive integer ends with 1, then it is referred as the no. of Game.
As example shown as follow :
13 = 1^2 + 3^2 = 1+9 = 10 Step:1
10 = 1^2 + 0^2 = 1+0 = 1 Step:2, iteration ends in Step 2 since number ends with 1

Then in next round ;
the contestants are asked to combine their newly invented number, i.e. No. of Game with prime number.
Now, being a intelligent  programmer, WAP to help the contestants to find out the Nth combined number within any given range.

Input Format

i/p consisting of THREE integers as follow X, Y, N.
one on each line
X & Y are upper limits  and lower limits  of the range and Find Nth number in range [X,Y].

 Line 1	 X,which is upper limit of the range
 Line 2	 Y,which is lower limit of the range
 Line 3	 N ,where Nth element of the series is necessary 

Constraints
X <= Y
X > 0
N > 0
Output Format

o/p will show the Nth element of the combined series lying in the given  range between X & Y.

Sample Input and Output

SNo.	Input	 Output
1	    1           19
        30
        3	
2	    12          No number is present at this index
        33
        5	
3	    -5          Invalid Input
        @
        4	


"""
import math

def opr(n):
    #print("in opr, n=",n)
    while True:
        
        s=0
        while n>0:
            x=n%10
            s=s+ x**2
            n=n//10
        if(s==1):
            #print("out while, s=",s)
            return s
        elif(s==4 or s==16 or s==37 or s==58 or s==89 or s==145 or s==42 or s==20 ):
            #print("out while, s=",4)
            return 4
        else:
            n=s
            #print("n=",n)



def isPrime(n):
    
    if(n<2):
        return False
    
    if n==2:
        return True
    
    if n%2==0:
        return False
    
    s=3
    rootn=int(math.sqrt(n))
    for i in range(s,rootn+1,2):
        if(n%i==0):
            return False
    else:
        return True













try:
    x=int(input().strip() )
    y=int(input().strip() )
    n=int(input().strip() )
except:
    print("Invalid Input")
    exit(0)

c=0
for i in range(x,y):
    
    if( isPrime(i) and opr(i)==1):
        
        c=c+1
        #print("c=",c,"i=",i)
        if(c==n):
            print(i)
            break
else:
    print("No number is present at this index")


