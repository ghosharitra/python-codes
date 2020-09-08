"""

Problem Description
Arnold is planning to follow a diet suggested by his Nutritionist. The Nutritionist prescribed him the total protein, carbohydrates and fats, he should take daily. Arnold searches on an online food store and makes a list of protein, carbohydrates and fats contained in a single unit of various food items.
His target is to have the maximum protein, carbohydrates and fats in his diet without exceeding the prescribed limit. He also wants to have as much diverse food items as much as possible. That is, he does not want to have many units of one food item and 0 of others. Multiple combinations of 'units of food items' are possible to achieve the target. Mathematically speaking, diversity is more if the difference between the number of units of food item chosen the most and the number of units of another food item chosen the least, is as small as possible.
To solve this problem, he uses maximum possible number of units of all the items so that total amount of protein, carbohydrates and fats is not more than prescribed limit. For example - if total nutrition required is 100P, 130C and 130F (where P is Protein, C is Carbohydrates and F is Fats) and 2 different food items, viz. Item A and Item B, have following amount of nutrition:
Item A - 10P, 20C, 30F
Item B - 20P, 30C, 20F
then, he can have (maximum possible) 2 units of all the items as having 3 units will exceed the prescribed amount of Carbohydrates and fats.
Next, he chooses food items to fulfill the remaining nutrients. He chooses one more units of maximum number of food items. He continues this process till he cannot add a unit of any food item to his diet without exceeding the prescribed limit. In this example, he can choose one more unit of item B or one more unit of item A. In case he has two sets of food items then the priority is given to fulfill the requirements of Protein, Carbohydrates, and Fats in that order. So he chooses item B.
You will be provided the maximum nutrients required and the nutrients available in various food items. You need to find the amount of nutrients for which there is a shortfall as compared to the prescription, after making his selection using the process described above. In the example he still needs 20P, 0C, 10F to achieve his target.
Constraints
Number of Food Items <= 10
Maximum amount of Nutrients is less than 1500 i.e. x +y + z <= 1500
Amount of P, C, F in two food items will not be same
P, C, F values in input can be in any order
Output should be in order - P, C, F.
Input
First line contains the maximum limit of nutrients in the following format.
xP yC zF, where x, y and z are integers
Second line contains nutrient composition of different food items separated by pipe (|).
Output
Print the shortfall for each nutrient type, fulfilled separated by space.
E.g. If the output is 10P, 20 C, 30 F, then print "10 20 30" (without quotes).
Time Limit
1
Examples
Example 1
Input
100P 130C 130F
10P 20C 30F|20P 30C 20F
Output
20 0 10
Explanation
Having 2 units of item A and 3 units of item B provides - 2 * [10P 20C 30F] + 3 * [20P 30C 20F] = 100P, 130C, 120F. This is the best combination that can reduce the shortfall [20P, 0C, 10F] without exceeding his prescription. In contrast, if 3 units of A and 2 units of B are chosen then 3 * [10P 20C 30F] + 2 * [20P 30C 20F] = 70P, 120C, 130F produces a shortfall of [30P, 10C, 0F]. However, since protein shortfall in this case is more than the previous combination, this is not the right combination to follow.
Example 2
Input
130P 120C 110F
7P 1C 3F|4P 9C 2F|4P 3C 2F
Output
2 4 50
Explanation
Having 9 units of item A, 9 units of item B and 8 units of Item C provides - 9 * [4P 9C 2F] + 9 * [4P 3C 2F] + 8 * [7P 1C 3F] = 108P, 116C, 60F. This is the best combination that can reduce the shortfall [2P, 4C, 50F] without exceeding his prescription.

"""

# MORE OPTIMIZED






di={}
def combine(asd,items,shortfall,minm=[99999]*3):
    
    print("asd:",asd,"shortfall:",shortfall)

    if(tuple(shortfall) in di.keys()):
        print("***********************************shortfall:",shortfall)
        return 


    for i in range(3):
        if(shortfall[i]<0):
            print(">>>break<<<")
            return -1
            

    for item in items:
        for i in range(3):
            shortfall[i]-=item[i]
        print("asd:",asd,"minm:",minm)


        flag=combine(asd+1,items,shortfall,minm)
        
        
        for i in range(3):
            shortfall[i]+=item[i]        

        if(flag==-1):
            if (minm[0]>=shortfall[0] and minm[1]>=shortfall[1] and minm[2]>=shortfall[2]):
                for i in range(3):
                    minm[i]=shortfall[i] 
            elif (minm[0]>=shortfall[0] and minm[1]>=shortfall[1] and minm[2]<shortfall[2]):
                for i in range(3):
                    minm[i]=shortfall[i] 
            elif (minm[0]>=shortfall[0] and minm[1]<shortfall[1] and minm[2]<shortfall[2]):
                for i in range(3):
                    minm[i]=shortfall[i] 
    
    di[tuple(shortfall)]=1
    print("ret||","shortfall:",shortfall,"asd:",asd,"minm:",minm)
    return minm
            
              
    
            



ip=input().split()
target=[0]*3
for t in ip:
    if t[-1]=="P":
        target[0]=int(t[:-1])
    elif t[-1]=="C":
        target[1]=int(t[:-1])
    elif t[-1]=="F":
        target[2]=int(t[:-1])
        
ipx=input().split("|")

items=[]
for ip in ipx:
    temp=[0]*3
    ip=ip.split()
    for t in ip:
        if t[-1]=="P":
            temp[0]=int(t[:-1])
        elif t[-1]=="C":
            temp[1]=int(t[:-1])
        elif t[-1]=="F":
            temp[2]=int(t[:-1])
    items.append(temp)

print(target)
print(items)

sum=[0]*3
for item in items:
    sum[0]+=item[0]
    sum[1]+=item[1]
    sum[2]+=item[2]

res=min(target[0]//sum[0],target[1]//sum[1],target[2]//sum[2])
shortfall=[0]*3
for i in range(3):
    shortfall[i]=target[i]-(res*sum[i])

shortfall=combine(0,items,shortfall)
print("di:",di)
for i in range(3):
    print(shortfall[i],end=" ")


