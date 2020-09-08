"""
Decode the logic &  print the Pattern that corresponds to given i/p . 
If N is equal to 3
then pattern will  be like :
10203010011012
**4050809
****607
If N= 4
then pattern will be like :
1020304017018019020
**50607014015016
****809012013
******10011 

Constraints
2 <= N <= 100 
Input Format
Single Integer N
Output 
The pattern 

Explanation 
Example 1
Input
3

Output
10203010011012
**4050809
****607
 
Example 2

Input
4
 
Output
1020304017018019020
**50607014015016
****809012013
******10011

"""

def sol(n):


    star=""
    line=""
    start=1
    end=n*(n+1)
    while n>0:
        
        sline=""
        for i in range(n):
            sline=sline+str(start)
            start+=1
            if(i!=n-1):
                sline=sline+"0"
        #print("sline:",sline)

        eline=""
        for i in range(n):
            eline="0"+str(end)+eline
            end-=1
        #print("eline:",eline)
        line=line+star+sline+eline+"\n"

        #print("line:",line)

        star=star+"**"
        n=n-1

    return line




try:
    n=int(input())
except:
    print("Invalid Input")
    exit(0)

res=sol(n)
print(res)