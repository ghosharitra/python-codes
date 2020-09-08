"""

input:  abc

output: cc
        reduced length: 2

input:  bbbbbba

output: a
        reduced length: 1



input:  cccabbbb

output: bbbbb
        reduced length: 5


input:  bbbabbcabac

output: a
        reduced length: 1
explaination:
l: 0 s1: ['b', 'b', 'b', 'a', 'b', 'b', 'c', 'a', 'b', 'a', 'c']
l: 1 s1: ['b', 'b', 'b', 'a', 'b', 'b', 'c', 'a', 'b', 'a', 'c']
l: 2 s1: ['b', 'b', 'b', 'a', 'b', 'b', 'c', 'a', 'b', 'a', 'c']
l: 1 s1: ['b', 'b', 'c', 'b', 'b', 'c', 'a', 'b', 'a', 'c']
l: 0 s1: ['b', 'a', 'b', 'b', 'c', 'a', 'b', 'a', 'c']
l: 0 s1: ['c', 'b', 'b', 'c', 'a', 'b', 'a', 'c']
l: 0 s1: ['a', 'b', 'c', 'a', 'b', 'a', 'c']
l: 0 s1: ['c', 'c', 'a', 'b', 'a', 'c']
l: 1 s1: ['c', 'c', 'a', 'b', 'a', 'c']
l: 0 s1: ['c', 'b', 'b', 'a', 'c']
l: 0 s1: ['a', 'b', 'a', 'c']
l: 0 s1: ['c', 'a', 'c']
l: 0 s1: ['b', 'c']
l: 0 s1: ['a']
a
reduced length: 1



"""


def sol(s1,l=0):
    print("l:",l,"s1:",s1)
    if l==len(s1)-1:
        return True,s1

    while True:
        
        if s1[l]==s1[l+1]:
            flag,s1=sol(s1,l+1)
            print("l:",l,"s1:",s1)
            if(flag):
                break
        else:

            if (s1[l]=='a' and s1[l+1]=='b' )or(s1[l]=='b' and s1[l+1]=='a' ):
                s1[l+1]='c'
                s1=s1[:l]+s1[l+1:]
            elif (s1[l]=='c' and s1[l+1]=='b' )or(s1[l]=='b' and s1[l+1]=='c' ):
                s1[l+1]='a'
                s1=s1[:l]+s1[l+1:]
            elif (s1[l]=='a' and s1[l+1]=='c' )or(s1[l]=='c' and s1[l+1]=='a' ):
                s1[l+1]='b'
                s1=s1[:l]+s1[l+1:]
            if l!=0:
                return False,s1
            else:
                print("l:",l,"s1:",s1)
                if l==len(s1)-1:
                    return True,s1
    
    return True,s1





s=list(input())
n=len(s)
flag,s=sol(s)
for i in s:
    print(i,end="")
print("\nreduced length:", len(s))
