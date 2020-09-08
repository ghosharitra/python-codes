"""
IST = UTC + (24/360)*82.5 = UTC + 5:30Hrs
find the smaller angle between hour and minute hand

"""

def UTCtoIST(utc,degree):
    ist=[0,0]
    val=(24/360)*degree
    ist[0]=utc[0]+int(val)
    ist[1]= utc[1] + (val-int(val))*60
    ist[0]=ist[0] + ist[1]//60
    ist[1]=ist[1]%60
    ist[0]=ist[0]%12
    if(ist[0]==0):
        ist[0]=12
    ist=list(map(int,ist))
    return ist
    


def clockAngle(ist):
    h=ist[0]
    m=ist[1]
    angle=abs(m-(h*5 + m/12))*6
    if(angle-int(angle)==0):
        angle=int(angle)
    if(angle>180):
        angle=360-angle
    
    return angle
        






try:
    h,m=map(int,input("enter utc time: ").split(':'))
    h=h+m//60
    m=m%60
    h=h%12
    if(h==0):
        h=12
    utc=[h,m]
    utc=list(map(int,utc))
    degree=float(input("enter degree of difference from utc: "))%360


    
except:
    print("-1")
    exit(0)
if h>12:
    print("-1")
    exit(0)

print(utc)
ist=UTCtoIST(utc,degree)
print(ist)

res=clockAngle(ist)
print(res)




