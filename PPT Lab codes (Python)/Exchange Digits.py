"""
Compute the nearest larger number by interchanging its digits updated.Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible print -1.

Input Format
2 numbers a and b, separated by space.
Output Format
A single number greater than b.
If not possible, print -1

Constraints
1 <= a,b <= 10000000

Example 1:

Sample Input:

    459 500

Sample Output:
    549

Example 2:

Sample Input:

    645757 457765

Sample Output:
    465577

"""

def asc(a):
    b=a.copy()
    b.sort()
    return b

def desc(a):
    b=a.copy()
    b.sort(reverse=True)
    return b

def conInt(a,r=[]):
    s=""
    for i in r:
        s=s+str(i)
    for i in a:
        s=s+str(i)
    b=int(s)
    return b


def solution(a,b,r=[],l=0):
    print("*************** level =",l," ***************")
    x=asc(a)
    y=desc(a)

    if conInt(y,r)<=conInt(b):
        print("---fail---","\nlevel =",l,"\nconInt(desc(a),r) =",conInt(y,r),"\nconInt(b) =",conInt(b))
        return -1
    elif conInt(x,r)>conInt(b):
        
        print("level =",l,"\nconInt(asc(a),r) =",conInt(x,r),"\nconInt(b) =",conInt(b))
        return conInt(x,r)
        
    else:
        for i in range(len(x)):
            if x[i]>=b[l]:
                r.append(x.pop(i))
                res=solution(x,b,r,l+1)
                if res==-1:
                    x.append(r.pop())
                    x.sort()
                else:
                    return res
                
            





a,b=input().split()
a=list(map(int,list(a)))
b=list(map(int,list(b)))
print(a,b)


res=solution(a,b)
print(res)