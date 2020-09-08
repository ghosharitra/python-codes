"""

Question -: Print a line containing all the divisors in increasing order separated by space.

Input Format: The first line of input contains an integer ‘N’ denoting the number.

Output Format: Print a line containing all the divisors in increasing order separated by space.

Constraints:
1 <= N <= 10^8

S.no	Input	Output	 
1	    10	    1 2 5 10

"""


try:
    n=int(input())
except:
    print("Invalid Input")
    exit(0)


count=0

i=1

factors=[]
    
while True:
    if n%i==0:
        j=n//i
        
        if j!=i:
            factors.insert(count//2,i)
            factors.insert(count//2 + 1,j)
            count+=2
            
        else:
            factors.insert(count//2,i)
            count+=1
        #print(factors)
    i+=1
    #print("i=",i,"j=",j)
    
    
    if(i>=j):
        break


print(factors)


