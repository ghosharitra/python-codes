f=open('MyData','r')

#print(f.read()) #cant print the lines in for loop if read it once
f1=open('ABC','a')
for data in f:
    print(data,end='')
    f1.write(data)

f2=open('image.jpg','rb')
f3=open('copy image.jpg','wb')
for data in f2:
    print(data,end='')
    f3.write(data)