number=input()

def baseToDecimal(number,base):
    weight=1
    decimal=0
    while number > 0:
        a = number % 10
        decimal = decimal + a*weight
        weight=weight*base
        number=number//10
    #print("decimal:",decimal)
    return decimal

def solution2(number,base1,base2=99999999):

    #print("number:",number)
    if base1==base2:
        print("if 1")
        return number

    base2=base1
    n=number
    max=n%10
    while n>0:
        b=n%10
        if b>max:
            max=b
        n=n//10
    base1=max+1
    print("base1:",base1,"base2:",base2)
    
    print("starting base:",base1)
    number=baseToDecimal(number,base1)
    number=solution2(number,base1,base2)
    print("returned base:",number)
    return number




def solution1(number):
    
    number=str.upper(number)
    base=0
    mx=0
    for i in number:
        if (65<=ord(i) and ord(i)<=90):
            if (ord(i)-55)>mx:
                mx=(ord(i)-55)
            
        elif (48<=ord(i) and ord(i)<=57):
            if (ord(i)-48)>mx:
                mx=(ord(i)-48)
    base=mx+1
    print("base:",base)

    no=0
    for i in number:
        if 65<=ord(i) and ord(i)<=90:
            no=no*base+(ord(i)-55)
        elif (48<=ord(i) and ord(i)<=57):
            no=no*base+(ord(i)-48)
    print("initial number:",no)
    res=solution2(no,base)
    return res





result=solution1(number)
print(result)