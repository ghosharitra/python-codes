"""

In NASA, 2 researchers, Mathew & John, started their work on a brand new planet, but while practicing on that research they faced a mathematical issue . In order to save the time Mathew & John divided their work. So NASA scientist Mathew worked on a piece & invented a number  calculated with the following formula:  
NASA researcher Mathew number is computed as follows by  using the following formula: H(n) = n(2n-1) 
NASA scientist John invented another number which is built by the following formula which is also called as John number. T(n) = n(n+1)/2 
Now NASA, 2 researchers ,Mathew & John are jumbled while combining their work. Now help Mathew & John combine their research work by searching out number in a given range that satisfies both properties. Using the above formula, the 1st few NASA researcher Mathew-John numbers are: 1 6 15 28 …
Input Format

i/p consists of THREE integers as follow : T1 ,T2 and M separated by space .
T1 upper limits  & T2 are  lower limits of the range. The range is inclusive of both T1 & T2. Find Mth number in the range [T1,T2] which is actually a  NASA researcher Mathew-John number.

Constraints
0 < T1 < T2 < 1000000

Output Format

Print out Mth number from formed sequence between T1 & T2 :


SNo.	Input	Output
1     90 150 2    120
2	  20 80  6	  No number is present at this index
3	  -5  3  a	  Invalid Input

"""

#this would be more efficient if we just print the mth mathew number as the output as all mathew no. are john no. but not vice versa



def john(n):
    return n*(n+1)//2 


def Mathew(n):
    return n*(2*n-1)



try:
    t1,t2,x=map(lambda s: int(s.strip()), input().strip().split()) # use split() in case of spliting with space, and use split(',') in case of comma separator
    if(t1>t2 or x>(t2-t1) ):
        raise Exception

except: 
    print("Invalid Input")
    exit(0)


i=0
jn=[]
mt=[]
while True:
    n1=john(i)
    if( t1<=n1 and n1<=t2):
        jn.append(n1)
    if( n1>t2 ):
        break
    i=i+1


i=0
while True:
    n2=Mathew(i)
    if( t1<=n2 and n2<=t2):
        mt.append(n2)
    if( n2>t2 ):
        break
    i=i+1


m=len(jn)
n=len(mt)

i=0
j=0
c=0
res=-1
while i<m and j<n:

    if(jn[i]<mt[j]):
        i=i+1

    elif(jn[i]==mt[j]):
        if( c==x-1 ):
            res=jn[i]
            break
        c=c+1
        i=i+1
        j=j+1


    elif(jn[i]>mt[j]):
        j=j+1

print("mathew: ",mt)
print("john: ",jn)
print("res: ",res)

try:
    if res==-1:
        raise Exception
    print(res)
except: 
    print("No number is present at this index")
    exit(0)