#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    maxdiff=0
    n=len(arr)
    substr=[]
    for i in range(n):
        temp=[]
        for j in range(0,i+1):
            if i==j:
                temp.append([arr[i]])
            elif(i-1==j):
                if( abs(arr[i]-arr[j])<2 ):
                    l=[arr[i],arr[j]]
                    temp.append(l)
                    maxdiff=len(l)
                else:
                    temp.append(-1)
            else:
                temp.append([])

        substr.append(temp)
    

    for i in range(n):
        for asd in substr[i]:
            print(asd,end="\t")
        print()
    print("maxdiff:",maxdiff)



    maxi,maxj=0,0
    for i in range(2,n):
        for j in range(i,n):
            #print("in for")
            # print("i:",i,"j:",j,"   j:",j,"j-i+1:",j-i+1)
            # print("arr[j]:",arr[j],"arr[j-i+1]:",arr[j-i+1])
            # print("substr[j-1][j-i+1]:",substr[j-1][j-i+1])

            if(substr[j-1][j-i]!=-1 and arr[j] in substr[j-1][j-i] ):
                # print("substr[j][j-i]:",substr[j][j-i])
                # print("substr[j-1][j-i+1]:",substr[j-1][j-i+1])
                
                substr[j][j-i]=substr[j-1][j-i]
                if((j)-(j-i)+1>maxdiff):
                    maxdiff=(j)-(j-i)+1
                    maxi=j
                    maxj=j-i
            else:
                substr[j][j-i]=-1


    print("\n\n\n")
    for i in range(n):
        for asd in substr[i]:
            print(asd,end="\t")
        print()


    print(maxj,maxi)
    print("maxdiff:",maxdiff)
    print( arr[ maxj:maxi+1 ] )
    return maxdiff



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
