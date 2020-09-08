# pattern:
#    a
#   bc
#  def
# ghij


# ord( ) to convert char to ascii
# chr( ) to convert ascii to char (basically string type with one digit)
a = 'a'
n = int(input("enter a no: "))


for i in range(n):
    for j in range(0, n-(i+1), 1):
        print(" ", end="")

    for j in range(0, i+1, 1):
        print(a, end="")
        a = chr(ord(a) + 1)
    print()
