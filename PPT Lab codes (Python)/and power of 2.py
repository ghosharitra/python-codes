#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countPairs(arr):
    # Write your code here
    odds=[]
    even=0
    odd=0
    # for i in arr:
    #     if(i&1==0):
    #         even+=1
    #     else:
    #         odd+=1
    #         odds.append(i)
    
    # n=len(odds)
    # res=0
    # for i in range(n):
    #     for j in range(i,n):
    #         if i&j==1:
    #             res+=1
            
    # print(even,odd)
    # print(res)
    # print(even*(even-1)//2)
    # print(even*odd)
    # return res+ (even*(even-1)//2) + (even*odd)

    n=len(arr)
    res=0
    for i in range(n):
        for j in range(i+1,n):
            s=0
            asd=bin(arr[i]&arr[j])[2:]
      #      print("i:",i,"a[i]:",arr[i],"j:",j,"a[j]:",arr[j],asd)
            for x in asd:
                s=s+int(x)
                if(s>1):
                    break
            
            if s==1:
     #           print(i,j)
                res+=1
    #print(res)
    return res


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
