# 100.1.2.35/20

l = input().split("/")
block = int(l[1])
ip = l[0]
ip = list(map(int, ip.split(".")))

n = 32 - block
s = ""
for i in range(4):
    s = s + bin(ip[i])[2:].zfill(8)

s = s[:block] + ('0' * n)

res = []
string = ""
for i in range(4):
    dec = 0
    for j in range(8):
        dec = 2 * dec + int(s[i * 8:(i * 8) + 8][j])

    string = string + "." + str(dec)
string = string[1:]
print("ip:", string, " to ", end="")

s = s[:block] + ('1' * n)

res = []
string = ""
for i in range(4):
  dec = int(s[i * 8:(i * 8) + 8], 2)
  string = string + "." + str(dec)
string = string[1:]
print("ip:", string)
