s = input("enter a sentence: ")
l=s.split()
for i in l:
    if len(i)>=3:
        print(i)