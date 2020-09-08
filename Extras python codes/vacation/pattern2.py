# pattern:
#     1 2 3 4
#   5 6 7
#  8 9
# 10


# ord( ) to convert char to ascii
# chr( ) to convert ascii to char (basically string type with one digit)
a = 1
n = int(input("enter a no: "))


for i in range(n):
    for j in range(0, n-(i+1), 1):
        print(" ", end="")

    for j in range(0, n-i, 1):
        print(a, " ", end="")
        a += 1
    print()
