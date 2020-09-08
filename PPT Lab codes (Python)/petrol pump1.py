n = int(input())
stopInfo = []
for i in range(n):
    stopInfo.append(list(map(int, input().split())))
#print(stopInfo)



start=0
flag = 0
tank = 0
count = 0
i = start
while count < n:
    tank = tank + stopInfo[i][0]
    if tank < stopInfo[i][1]:
        tank=tank+stopInfo[start][1]-stopInfo[start][0]
        start+=1
        count-=1
        flag=0
    else:
        tank=tank-stopInfo[i][1]

    if i == n - 1:
        i = 0
    else:
        i += 1
    count += 1
    if count == n:
        flag = 1

if flag == 1:
    print(start)
else:
    print("-1")

"""

3
1 5
10 3
3 4




3
6 4
3 6
7 3

"""
