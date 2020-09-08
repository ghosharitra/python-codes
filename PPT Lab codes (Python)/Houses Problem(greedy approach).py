"""
Question:- There are n houses build in a line, each of which contains some value in it.

 A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two neighbours left and right side.

What is the maximum stolen value?

Sample Input: val[] = {6, 7, 1, 3, 8, 2, 5}

Sample Output: 20

"""
def sol(houses,n,num=0,m=0):
    print("houses:",houses,"num:",num,"m:",m)
    val=max(houses)
    if(val==0):
        print("num:",num)
        if(m<num):
            m=num
        return m


    
    for i in range(n):
        if(houses[i]==val):
            print("i:",i)
            houses[i]=0

            if(i+1<n):
                print("try1",i+1)
                x=houses[i+1]
                houses[i+1]=0



            if(0<=i-1):
                print("try2",i-1)
                y=houses[i-1]
                houses[i-1]=0

            print("-->",houses)

            m=sol(houses,n,num+val,m)
            

            houses[i]=val
            if(i+1<n):
                houses[i+1]=x
            if(0<=i-1):
                houses[i-1]=y

            
    return m


houses=list(map(int,input().split() ))
n=len(houses)
res=sol(houses,n) 
print(res)