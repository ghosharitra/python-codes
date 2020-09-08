s=input("enter a sentence: ").split()
longest=s[0]
max=len(s[0])
for i in s:
  if len(i)>max:
    max=len(i)
    longest=i
    
print(longest)