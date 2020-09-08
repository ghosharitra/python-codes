"""

Find CRC.

Input Format

Length of Dataword(n)

Dataword

Length of Divisor(m)

Divisor

Constraints

n >=2 <= 16

m>=1 <= 6

Output Format

CRC

Sample Input 0

7
1010000
44

1001
Sample Output 0

011
Explanation 0

Fist line of input is length of Data input Data Length of Crc Generator or Divisor Crc Generator


14
11010110110000
5
10011







6
110011
4
1011

"""


def xor(temp,crc,n):
  res=[]
  for i in range(n):
    res.append(0)
  for i in range(n):
    if temp[i]==crc[i]:
      res[i]='0'
    else:
      res[i]='1'
  return res


m=int(input("enter no. of bits in dataword: "))
word=list(input("enter dataword: ")[0:m])
#print("word: ",word)

n=int(input("enter no. of bits in crc: "))
crc=list(input("enter crc: ")[0:n])
#print("crc: ",crc)

m=m+n-1
for i in range(n-1):
  word.append('0')
#print("word: ",word)


res=[]
zero=[]
for i in range(n):
  res.append('0')
  zero.append('0')

temp=word[0:n]

#print("temp: ",temp)


for i in range(m-n+1):
#  print("temp:", temp)
  if temp[0]!='0':
#    print("crc:",crc)
    res = xor(temp, crc,n)
  else:
#    print("crc:", zero)
    res = xor(temp, zero,n)
#  print("res:", res)
  for j in range(n-1):
    temp[j]=res[j+1]
  if n+i<len(word):  
    temp[n-1]=word[n+i]

res=res[1:n]
from functools import reduce
rem=reduce(lambda s1,s2: s1+s2,res)
sent=reduce(lambda s1,s2: s1+s2,word[0:(m-n+1)])+rem
print("remainder: ",rem)
print("sent dataword: ",sent)
