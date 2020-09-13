import math
a=int(input("enter start of the range: "))
b=int(input("enter end of the range: "))

for i in range(a,b+1):
    print(len(str(math.factorial(i))))