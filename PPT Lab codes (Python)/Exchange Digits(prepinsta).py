#import itertools to get permutation function
from itertools import permutations
#take inputs
num1 = int(input('Enter the 1st number :'))
num2 = int(input('Enter the 2nd number :'))
#initialize a flag variable
flag = 0
#convert num1 to string list
num1 = list(str(num1))
#sort the list
num1 = sorted(num1)
#find all permutations
perm = permutations(num1) 
#iterate through all permutations 
for i in list(perm): 
    #initialize an string
    string = " "
    #iterate through an string
    for j in i:
        string+=j
    #typecast string to integer
    #check for next greater value
    if int(string) > num2:
        #if True Change the flag variable 
        #break the loop
        flag = 1
        break
#check if the number is found or not
if flag == 1:
    print(string)
else:
    print(-1)