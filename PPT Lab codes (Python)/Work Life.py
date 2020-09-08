"""
Jay works for support project where Jay has to resolve some tickets each day denoted by A[i] . Jay  knows, ahead of time, the no. of tickets for each day for N days. Let X be an array of length N. 
Each element X[i]  where i=1 to i=N describe no. of tickets to resolve on its ith day. 
Jay is struggling to balance his work life. On some days, workload is huge & on other days, it is very little. Now Jay can procrastinate & choose to postpone up to  K  tickets to next day. However, tickets can only be postponed once 
Find optimal solution where workload must be distributed as evenly as possible with above constraints and also print the maximum no. of tickets jay needs to resolve on given days.
 Constraints
1 <= T <= 50
1 <= N <= 100
1 <= K <= 100
1 <= X[i] <= 10^9
Input Format
First line : T no. of test cases.
For each T :
First line : N K described above
Next line :  N spaced int denoting no. of tickets for every day 
Output 
For each test case T , print a single integer per line describing maximum no. of tickets Jay have  to resolve after optimal rearrangement with above constraints.

Explanation 

Example 1

Input
2
3 100
3 1 2
28 31 37
3 15 32
Output
2
37

Explanation
Initially highest workload is on 1st day 3 tickets. Now 1 ticket should be postponed from day 1 to day 2. So array is [2,2,2] & maximum workload is Two . For Second test case, no rearrangement is required, Therefore  the o/p  is 37.
 
Example 2
Input
1
3 100
7 1 1

Output
4

Explanation
Initially highest workload is on 1st day 7 tickets. Now we postpone 4 tickets from day 1 to day 2. Array now looks like [3,5,1]. Now on day 2, even K is 100, we can only postpone 1 ticket since tickets can only be postponed once. In other words, 4 tickets out 5 which were postponed from day 1 has to be resolved on day 2. They cannot be postponed any further. So after postponing 1 ticket array looks like [3,4,2] & maximum workload is 4, Therefore answer is 4 

"""

def isPossible(tickets,tlen,m,postpone):
    add=0
    for i in range(tlen):

        if tickets[i]+add<=m:
            add=0
            continue
        
        rem=0
        rem=min(tickets[i]+add-m,postpone)
        if(tickets[i]-rem<0):
            return False
        if(tickets[i]+add-rem>m):
            return False
        add=rem
    if(add!=0):
        return False
    else:
        return True


def sol(t,tlen,postpone,info):
    res=[]
    for i in range(t):
        tickets=info[i]
        ll=1
        ul=max(tickets)
        best=ul
        while(ll<=ul):
            mid=(ul+ll)//2
            if(isPossible(tickets,tlen,mid,postpone)):
                best=mid
                ul=mid-1
            else:
                ll=mid+1
        res.append(best)
    return res



try:
    t=int(input())
    tlen,postpone=map(int,input().split() )
    info=[]
    for i in range(t):
        temp=list(map(int,input().split() ))
        if len(temp)!=tlen:
            raise Exception
        info.append(temp)
except:
    print("Invalid Input")
    exit(0)

res=sol(t,tlen,postpone,info)
for i in range(t):
    print(res[i])