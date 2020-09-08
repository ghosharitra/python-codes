t=int(input())

for i in range(t):
    string=input().lower()
    freq=[0]*26
    for s in string:
        val=ord(s)-97
        freq[ val ]+=1
    for j in range(26):
       if(freq[j]!=0 and freq[j]!=j+1):
           print("No")
           break
    else:
        print("Yes")

