def oneToNine(x):
    if x==1:
        print("one",end=" ")
    elif x==2:
        print("two",end=" ")
    elif x==3:
        print("three",end=" ")
    elif x==4:
        print("four",end=" ")
    elif x==5:
        print("five",end=" ")
    elif x==6:
        print("six",end=" ")
    elif x==7:
        print("seven",end=" ")
    elif x==8:
        print("eight",end=" ")
    elif x==9:
        print("nine",end=" ")



def twentyToNinety(x):
    
    if x==2:
        print("twenty",end=" ")
    elif x==3:
        print("thirty",end=" ")
    elif x==4:
        print("fourty",end=" ")
    elif x==5:
        print("fifty",end=" ")
    elif x==6:
        print("sixty",end=" ")
    elif x==7:
        print("seventy",end=" ")
    elif x==8:
        print("eighty",end=" ")
    elif x==9:
        print("ninty",end=" ")






def tenToNineteen(x):
    if x==10:
        print("ten",end=" ")
    elif x==11:
        print("eleven",end=" ")
    elif x==12:
        print("twelve",end=" ")
    elif x==13:
        print("thirteen",end=" ")
    elif x==14:
        print("fourteen",end=" ")
    elif x==15:
        print("fifteen",end=" ")
    elif x==16:
        print("sixteen",end=" ")
    elif x==17:
        print("seventeen",end=" ")
    elif x==18:
        print("eighteen",end=" ")
    elif x==19:
        print("ninteen",end=" ")




number=input()

if number=='0':
  print("zero")



number=number.zfill(5)
no=list(number)






if no[-5]!='0':
    if no[-5]=='1': 
        tenToNineteen(int(no[-5] +no[-4]))
    else:
        twentyToNinety(int(no[-5]))
        if no[-4]!='0':
            oneToNine(int(no[-4]))       
    print("thousand",end=" ")       
else:
    if no[-4]!='0':
       
        oneToNine(int(no[-4]))
        print("thousand",end=" ")

if no[-3]!='0':
    oneToNine(int(no[-3]))
    print("hundred",end=" ")

if no[-2]!='0':
    
    if no[-2]=='1': 
        tenToNineteen(int(no[-2]+no[-1]))
    else:
        twentyToNinety(int(no[-2]))
        if no[-1]!='0':
            oneToNine(int(no[-1]))       
          
else:
    if no[-1]!='0':
       
        oneToNine(int(no[-1]))
    













    