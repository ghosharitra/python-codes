number, k = [int(i) for i in input().split(",")]
factor = []
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count = count + 1
        factor.append(i)

if count < k:
    print("1")
else:
    print(factor[-k])