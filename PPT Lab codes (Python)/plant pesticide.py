"""
7
6 5 8 4 7 10 9


5
3 6 2 7 5
"""


n=int(input())
pesticideLevel = list(map(int, input().split()))

#print(pesticideLevel)
flag=0

count=-1
while flag==0:
    i = 0
    flag=1
    while i < len(pesticideLevel)-1:
        if pesticideLevel[i] < pesticideLevel[i+1]:
            del pesticideLevel[i+1]
            flag=0


        i+=1
    #print(pesticideLevel)

    count+=1


print(count)