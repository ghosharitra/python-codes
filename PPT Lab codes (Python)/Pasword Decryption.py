"""
51Pa*0Lp*0e
aP1pL5e

"""
def decryptPassword(s):

    l=list(s)
    #print(l)
    n=len(l)

    z=""
    i=0
    j=n-1
    while j>-1:
        if l[j]=="0":
            z=l[i]+z
            i+=1
            j-=1
        elif l[j]=='*':
            if l[j-1].islower() and l[j-2].isupper():
                z=l[j-1]+l[j-2]+z
                j=j-3
            else:
                z=l[j]+z
                j-=1


        elif( 49<=ord(l[j]) and ord(l[j])<=57):
            break
        else:
            z=l[j]+z
            j-=1

    #print(z)
    return z



s=input()
res=decryptPassword(s)
print(res)