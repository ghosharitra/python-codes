"""
input:
4 3
20 7 5 4

output:
17
"""
import math

def heapify(a,n):

    for i in range(n//2,0,-1):
        #print("\n\nin for\n\n")
        j=i
        
        while True:
            #print("in while")
            swap=0
            if((2*j-1)<n and (2*j<n) and ( a[2*j-1]>a[j-1] or a[2*j]>a[j-1] )):
                #print("a[j-1]=",a[j-1]," a[2*j-1]=",a[2*j-1]," a[2*j]=",a[2*j])
                if a[2*j-1]>a[2*j]:
                    t=a[2*j-1]
                    a[2*j-1]=a[j-1]
                    a[j-1]=t
                    swap=1
                    j=2*j
                else:
                    t=a[2*j]
                    a[2*j]=a[j-1]
                    a[j-1]=t
                    swap=1
                    j=2*j+1
            elif (2*j-1)<n and a[2*j-1]>a[j-1]:
                #print("a[j-1]=",a[j-1]," a[2*j-1]=",a[2*j-1])
                t=a[2*j-1]
                a[2*j-1]=a[j-1]
                a[j-1]=t
                swap=1
                j=2*j+1
            #print(a)
            if swap!=1:
                break
    #print("heapified:",a)






n,nopr=map(int,input().split())
arr=list(map(int,input().split()))

for i in range(nopr):
    heapify(arr,n)
    arr[0]=arr[0]//2  

print(sum(arr))








