"""
Problem Description
Three characters { #, *, . } represents a constellation of stars and galaxies in space. Each galaxy is demarcated by # characters. There can be one or many stars in a given galaxy. Stars can only be in shape of vowels { A, E, I, O, U } . A collection of * in the shape of the vowels is a star. A star is contained in a 3x3 block. Stars cannot be overlapping. The dot(.) character denotes empty space.
Given 3xN matrix comprising of { #, *, . } character, find the galaxy and stars within them.
Note: Please pay attention to how vowel A is denoted in a 3x3 block in the examples section below.
Constraints
3 <= N <= 10^5
Input
Input consists of single integer N denoting number of columns.
Output
Output contains vowels (stars) in order of their occurrence within the given galaxy. Galaxy itself is represented by # character.
Time Limit
1
Examples
Example 1
Input
18
* . * # * * * # * * * # * * * . * .
* . * # * . * # . * . # * * * * * *
* * * # * * * # * * * # * * * * . *
Output
U#O#I#EA
Explanation
As it can be seen that the stars make the image of the alphabets U, O, I, E and A respectively.
 
Example 2
Input
12
* . * # . * * * # . * .
* . * # . . * . # * * *
* * * # . * * * # * . *
Output
U#I#A
Explanation
As it can be seen that the stars make the image of the alphabet U, I and A.
 
"""

n=int(input())
space=[]
for i in range(3):
    temp=list(input().split())[:n]
    space.append(temp)


index=0
res=""
while(index<n):
    if space[0][index]=="#":
        res=res+"#"
        index+=1
        continue
    if space[0][index]==".":
        if space[1][index]==".":
                index+=1
                continue
        else:
            res=res+"A"
            index+=3
            continue
    else:
        if space[0][index+1]==".":
            res=res+"U"
            index+=3
            continue
        else:
            if space[1][index]==".":
                res=res+"I"
                index+=3
                continue
            else:
                if space[1][index+1]==".":
                    res=res+"O"
                    index+=3
                    continue
                else:
                    res=res+"E"
                    index+=3
                    continue

print(res)