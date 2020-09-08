n = int(input("no. of stops: "))
stopInfo = []
for i in range(n):
    stopInfo.append(list(map(int, input().split())))
print(stopInfo)



for start in range(n):
    flag = 0
    tank = 0
    count = 0
    i = start
    while count < n:
        tank = tank + stopInfo[i][0]
        if tank < stopInfo[i][1]:
            break
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
        break

else:
    print("none")

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
