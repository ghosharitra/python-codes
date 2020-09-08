#  255.255.240.0
ip=list(map(int,input().split(".")))
binip=""
for i in ip:
    binip=binip+bin(i)[2:]

s=0
for i in binip:
    s=s+int(i)
print("no. of host per subnet: ",(2**(32-s))-2)


nid=0
if ip[0]==255:
    nid=8
    print("no. of subnet in class A: ",2**(s-nid))
        
    if ip[1]==255:
        nid=16
        print("no. of subnet in class B: ",2**(s-nid))
    
        if ip[2]==255:
            nid=24
            print("no. of subnet in class C: ",2**(s-nid))
        else:
            print("no. of subnet in class C: Not Possible")
    else:
        print("no. of subnet in class B: Not Possible")
        print("no. of subnet in class C: Not Possible")
else:
    print("no. of subnet in class A: Not Possible")
    print("no. of subnet in class B: Not Possible")
    print("no. of subnet in class C: Not Possible")
