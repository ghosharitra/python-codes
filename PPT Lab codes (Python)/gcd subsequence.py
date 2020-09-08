#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#

def euclidianGCD(a,b):
    if b==0:
        return a
    return euclidianGCD(b,a%b)

def sol(numbers,n,k,select,gcd=0,l=0,maxgcd=-99999,arr=[],maxarr=[]):
    
    if(maxgcd>=gcd):
        return maxgcd

    if(l>=k and gcd >maxgcd):
        maxgcd=gcd
        maxarr=arr.copy()
        



    for i in range(n):

        if(select[i]==0):
            select[i]=1
            arr.append(numbers[i])
            if l==0:
                gcd=numbers[i]
            maxgcd,maxarr=sol(numbers, n, k, select,euclidianGCD(gcd,numbers[i]),l,maxgcd,arr,maxgcd)
            select[i]=0
            arr.pop()
    return maxgcd,maxarr


def findSubsequence(numbers, k):
    # Write your code here
    n=len(numbers)
    select=[0]*n
    
    gcd,arr=sol(numbers,n,k,select)
    print(gcd)
    print(arr)
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    k = int(input().strip())

    result = findSubsequence(numbers, k)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
