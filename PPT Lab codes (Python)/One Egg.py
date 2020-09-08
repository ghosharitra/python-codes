"""
Problem
"One Egg" is an egg supply company which supplies eggs to retailers. They have M classes of eggs. Each class can have N number of eggs (N can be same or can vary class to class).  They accept an order via mail for X eggs. In response, they confirm if they can supply the eggs with a "Thank you" note and the number of eggs or with a "Sorry" note and the numbers of eggs they can supply. They also mention the breakdown of eggs by class they will supply. The ordered eggs are adjusted against the different classes with the most number of eggs adjusted first then the balance is adjusted against the second highest and so on.   The company is a bit superstitious as well. If the number of eggs ordered is greater than or equal to the total number of eggs in stock then they retain one egg and responds back with the "Sorry" note with total number of eggs in stock minus one and breakdown of eggs by class.  

Note: If the classes have same number of eggs then class entered first should be selected to adjust. 
Input Format
 First line contains two space-separated integers denoting the respective values of M (the number of classes of eggs) and X, the number of eggs ordered  The following M lines contain an integer each indicating the number of eggs available in each class 
Output Format  
First line should be, if X is less than total number of Eggs then Print  " Thank you, your order for X eggs is accepted"  Else if X is greater than or equal to total number of Eggs then print "  " Sorry, we can only supply (total number of Eggs in stock -1) eggs"  T hen M lines with 3 columns:  First column - Number of eggs available in each class  Second column - Eggs allocated against each class for that order  Third column - Balance Eggs against each class
Constraints
 1 ≤ M ≤ 20  N ≥ 1  X ≥ 1
 
 
Example 1  
Input  
5 150  
50  
15  
80  
10  
5  

Output  
Thank you, your order for 150 eggs are accepted  
50         50        0  
15         15        0                      
80         80        0  
10         5         5          
5          0         5  

Explanation 
 Total order of 150 eggs is less than the total number of Eggs 50+15+80+10+5 = 160. Hence the Thank you message.  150 was first adjusted against Class with first highest number of eggs 80. Balance of 150-80 = 70 was adjusted against second highest class of 50. Balance of 70-50 = 20 then adjusted against 15. Balance of 20-15 = 5 then adjusted against 10 leaving behind 5 eggs in that class.
  
Example 2
  
Input 
 
4 250  
80  
50  
70  
20  

Output 

Sorry, we can only supply 219 eggs  
80        80        0  
50        50        0                      
70        70        0  
20        19        1           

Explanation 
Total order of 250 eggs was greater than the total number of eggs 80+50+70+20 = 220. Hence the sorry message.  250 was first adjusted against Class with first highest number of eggs 80. Balance of 250-80 = 170 was adjusted against second highest class of 70.   Balance of 170-70 = 100 was then adjusted against 50. Balance of 100-50 = 50 then adjusted against 20. Since Balance is greater than 
last class of egg all but one egg is left in that last class.

input:
4 250
155
50
20
50

output:
Thank you, your order for 250 eggs are accepted
155     155     0
50      50      0
20      0       20
50      45      5



"""
def sol(noOfClass,order,classStrength):
    info=[]
    res=[]
    for i in range(noOfClass):
        temp=[0]*4
        info.append(temp)
        temp=[0]*3
        res.append(temp)

    stock=0
    #print(info)
    for i in range(noOfClass):
        info[i][0]=i
        info[i][1]=classStrength[i]
        info[i][3]=classStrength[i]
        stock=stock+info[i][1]
    #print("unsorted:",info)
    msg=""

    # for i in range(noOfClass):
    #     for j in range(noOfClass-i-1):
    #         if info[j][1]<info[j+1][1]:
    #             t=info[j][0]
    #             info[j][0]=info[j+1][0]
    #             info[j+1][0]=t

    #             t=info[j][1]
    #             info[j][1]=info[j+1][1]
    #             info[j+1][1]=t

    #             t=info[j][3]
    #             info[j][3]=info[j+1][3]
    #             info[j+1][3]=t
    #info.sort(key=lambda x: print(x))
    #print(info)
    info.sort(key=lambda x: x[1],reverse=True)


    #print("sorted:",info)







    if(stock>order):
        msg="Thank you, your order for "+str(order)+" eggs are accepted"
        
        for i in range(noOfClass):
            if order>info[i][1]:
                order=order-info[i][1]
                info[i][2]=info[i][1]
                info[i][3]=0
            else:
                info[i][2]=order
                info[i][3]=info[i][3]-order
                order=0
                break
    else:
        msg="Sorry, we can only supply "+str(stock-1)+" eggs"
        order=stock-1
        for i in range(noOfClass):
            if order>info[i][1]:
                order=order-info[i][1]
                info[i][2]=info[i][1]
                info[i][3]=0
            else:
                info[i][2]=order
                info[i][3]=info[i][3]-order
                order=0
                break 
    

    for i in range(noOfClass):
        res[ info[i][0] ][0]=info[i][1]
        res[ info[i][0] ][1]=info[i][2]
        res[ info[i][0] ][2]=info[i][3]




    return msg,res

try:
    noOfClass,order=map(int,input().split())
    classStrength=[]
    
    if(noOfClass<1 or noOfClass>15 or order<1):
        raise Exception

    for i in range(noOfClass):
        val=int(input())
        if val<1:
            raise Exception
        classStrength.append(val)
except:
    print("Invalid Input")

#print(noOfClass,order,classStrength)
msg,res=sol(noOfClass,order,classStrength)

print(msg)
for i in range(noOfClass):
    for j in range(3):
        print(res[i][j],end="\t")
    print()