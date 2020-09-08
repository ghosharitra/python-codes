#bubble sort

def bubbleSort(a,n):
    
    for i in range(0,n):
        for j in range(0,n-1-i):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t


































#selection sort

def selectionSort(a,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if(a[min]>a[j]):
                min=j
        if min!=i:
            t=a[min]
            a[min]=a[i]
            a[i]=t


































#insertion sort

def insertionSort(a,n):
    for i in range(1,n):
        temp=a[i]
        j=i-1
        while( j>=0 and a[j]>temp):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp

































#merge sort

def merge(x,l,c,r):
    m=c-l+1
    n=r-c
    a=[]
    b=[]
    for i in range(m):
        a.append(x[l+i])
    for j in range(n):
        b.append(x[c+j+1])
    
    i=0
    j=0
    k=0
    while(i<m and j<n):
        if(a[i]<b[j]):
            x[l+k]=a[i]
            k=k+1
            i=i+1
            
        else:
            x[l+k]=b[j]
            k=k+1
            j=j+1
            
    
    while(i<m):
        x[l+k]=a[i]
        k=k+1
        i=i+1
        
        

    while(j<n):
        x[l+k]=b[j]
        k=k+1
        j=j+1
        
        




def mergeSort(a,n,l=0):
    
    r=n-1
    if(l==r):
        return
    m=(l+r)//2
    mergeSort(a,m+1,l)
    mergeSort(a,n,m+1)
    merge(a,l,m,n-1)

































#quick sort

def quickSort(a,n,l=0):
    print("l=",l,"r=",n-1)
    print("a[l:n]",a[l:n])
    r=n-1

    if l>=r:
        return


    pivot=l
    i=l
    j=r
    while(i<j):

        while i<r and a[i]<=a[pivot]:
            i=i+1

        while j>l and a[j]>=a[pivot]:
            j=j-1
        
        #print("i=",i,"j=",j)
        if i<j:
            
            t=a[i]
            a[i]=a[j]
            a[j]=t

    if j!=pivot:
        #print("pivot:",pivot)
        t=a[pivot]
        a[pivot]=a[j]
        a[j]=t

    


    quickSort(a,j+1,l)
    quickSort(a,n,j+1)
    

































#heap sort
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






    
    


def deleteHeap(a,n):
    r=n-1
    while(r>0):
        #print("in while")
        t=a[0]
        a[0]=a[r]
        a[r]=t
        
        n=n-1
        r=n-1
        j=1
        while True:
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

            if swap!=1:
                break
            #print("delete :",a)



def heapSort(a,n):

    heapify(a,n)    
    deleteHeap(a,n)

































#shell sort

def shellSort(a,n):
    
    gap=n//2
    while(gap>0):
        i=gap
        while(i<n):
            j=i-gap
            temp=a[i]
            while(j>=0 and a[j]>temp):
                a[j+gap]=a[j]
                j=j-gap
            a[j+gap]=temp
            i=i+1
        gap=gap//2


































#count sort

def countSort(a,n):
    
    min=a[0]
    max=a[0]
    for i in a:
        if(min>i):
            min=i
        if(max<i):
            max=i
    size=max-min+1
    count=[0]*size

    #print("COUNT: ",count)

    for i in a:
        count[i-min]=count[i-min]+1
    #print("COUNT: ",count)    
    for i in range(size-1):
        count[i+1]=count[i+1]+count[i]
    #print("COUNT: ",count)
    for i in range(size-2,-1,-1):
        count[i+1]=count[i]
    count[0]=0
    #print("COUNT: ",count)
    
    i=0
    while(i<size-1):
        if count[i]!=count[i+1]:
            a[count[i]]=i+min
            count[i]+=1
        else:
            i=i+1
    #print("i=",i,"count[i]=",count[i],"size=",n)
    while(count[i]<n):
        a[count[i]]=i+min
        count[i]=count[i]+1

































#radix sort

def radixSort(x,n):
    a=x.copy()
    pow=[]
    i=0
    p=10
    no_digits=1
    while i<n:
        if(a[i]//p!=0):
            p=p*10
            no_digits=no_digits+1
        else:
            i=i+1
    p=1
    for i in range(no_digits+1):
        pow.append(p)
        p=p*10
    
    

    for i in range(1,no_digits+1):
        count=[0]*10
    
        for j in a:
            value=((j % pow[i]) - (j % pow[i-1]))//pow[i-1]
            count[value]=count[value]+1
        

        for j in range(9):
            count[j+1]=count[j+1]+count[j]
        

        for j in range(8,-1,-1):
            count[j+1]=count[j]
        count[0]=0

        for j in range(n):
            value=((a[j] % pow[i]) - (a[j] % pow[i-1]))//pow[i-1]
            
            x[ count[value] ]=a[j]
            count[value]=count[value]+1

        #print(x)
        a=x.copy()

































#bucket sort 

def bucket(x,n,no_digits,pow,l=0,d=1):
    #print("x=",x,"n=",n,"no_digits=",no_digits,"pow=",pow,"l=",l,"d=",d)
    if d>no_digits or l>=n-1:
        return

    i=d
    a=x.copy()
    count=[0]*10
    #print("COUNT:",count)
    
    for j in a[l:n]:
        #print("(int)(j*pow[i])=",(int)(j*pow[i]),"(int)(j*pow[i-1])*10=",(int)(j*pow[i-1])*10)
        value=(int)(j*pow[i])-(int)(j*pow[i-1])*10
        count[value]=count[value]+1
    #print("COUNT:",count)

    for j in range(9):
        count[j+1]=count[j+1]+count[j]
    #print("COUNT:",count)

    for j in range(8,-1,-1):
        count[j+1]=count[j]
    count[0]=0
    start_pos=count.copy()
    #print("COUNT:",count)

    for j in range(l,n):
        value=(int)(a[j]*pow[i])-(int)(a[j]*pow[i-1])*10
        
        x[ l+count[value] ]=a[j]
        count[value]=count[value]+1

    #print(x)
    
    for i in range(9):
        bucket(x,l+start_pos[i+1],no_digits,pow,l+start_pos[i],d+1)




def bucketSort(a,n):
    
    pow=[]
    i=0
    p=1
    no_digits=0
    while i<n:
        if( (a[i]*p) % 1!=0):
            p=p*10
            no_digits=no_digits+1
        else:
            i=i+1
    p=1
    for i in range(no_digits+1):
        pow.append(p)
        p=p*10
    
    #print(no_digits,pow)

    bucket(a,n,no_digits,pow)



























# main function
#a=[100,4,63,2,1,78,1,4,54,1,63,54,102,2,4]
#n=15
#a=[10,5,20,40,15,120,20,30,40,125,46,24,65,34,30,65]
#n=16
#a=[10,5,12,20,15]
#n=5
#a=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
#n=17
#a=[54312,54,243,954,243]
#n=5
a=[0,0.001,0.154,0.33,0.87,0.747,0.52,0,0.354,0.18,0.35,0.13,0.742,0.435,0.325,0.3]
n=len(a)
#a=[1,2,4,2,4,0,0,5,3,3,5,3,2,0,4,2,3,4,2,0,4,2,1,3,1,2,2,1,2,2]
#n=30
print("unsorted array:",a," size:",n)
bucketSort(a,n)
print("  sorted array:",a," size:",n)