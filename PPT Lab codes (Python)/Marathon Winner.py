"""

Usually Race is generally organized by distance but this race is something interesting as it  will be organized by time.
In order to predict the winner of race  we will check each TWO sec.
Let’s say total race time is 7 sec so we will check for (7-1) sec.
For 7 sec : We will check who is leading at 2 second , 4 second & 6 second .
Participant who is leading more no. of times is winner of race  from prediction perspective.
Now our objective is to predict a winner in this marathon race .
Note:
1) At particular time let say at Fourth sec , top 2 (top N, in general) participants are at equal distance, then in this case both are leading we will increase count for both (all N).
2) And after calculating at all time slices, if number of times someone is leading, is same for two or more participants, then one who come ﬁrst in input sequence will be the winner.
 
For Example : If participant Two  & Three are both leading with equal  number, participant 2 will be the winner of race. 
 
 Constraint
1 <= T <= 100
1 <= N <= 100 
Input Format
First line : Number of participants N
Second line :  Total time in seconds of this Marathon as T
Next N lines are as follows :
We have T+1 integers split by space.
1st T integers are as follow:
ith integer describe the no. of steps taken by the participant at the ith sec.
T+1st integer describe the Distance in meters of each step. 
Output 
Index of Marathon winner note that index starts with 1. 

Explanation 
Input
3
8
2 2 4 3 5 2 6 2 3
3 5 7 4 3 9 3 2 2
1 2 4 2 7 5 3 2 4

 
Output
2
 
Explanation
 
3 <= No. of candidate
8 <= Total time of Sprint in sec
2 2 4 3 5 2 6 2 3 <= data for First candidate. First 8 integers describe no. of steps per sec & last integer describe distance covered in each step i.e. 3.
3 5 7 4 3 9 3 2 2 <= similarly, 2nd candidate’s data.
1 2 4 2 7 5 3 2 4  <= similarly, 3rd candidate’s data.
At time 2: Here Second marathoner is leading
12 (2*3+2*3)
16 (3*2+5*2)
12 (1*4+2*4)
At time 4 :Here also Second  marathoner is leading
33 ( 2*3+2*3 +4*3+3*3)
38
36
At time 6 :Here Third marathoner is leading
57
62
84
Output
2
Since, 2nd marathoner is leading more no. of times, hence 2 is the winner.

"""
def sol(noOfParticipants,totalTime,info):
    scores=[0]*noOfParticipants
    dist=[0]*noOfParticipants
    for i in range(0,totalTime-2,2):
        print("i=",i)
        maxval=-999999
        for j in range(noOfParticipants):
            dist[j]+=(info[j][i] + info[j][i+1] )*info[j][-1]
            if(maxval< dist[j] ):
                maxval= dist[j]
        
        for j in range(noOfParticipants):
            if maxval==dist[j]:
                scores[j]+=1
        print("dist:",dist)
        print("scores:",scores)
    return scores.index(max(scores))+1
        


try:
    noOfParticipants=int(input())
    totalTime=int(input())
    #totalTime+=1
    info=[]
    for i in range(noOfParticipants):
        temp=list(map(int,input().split() ))
        if len(temp)!=totalTime+1:
            raise Exception
        info.append(temp)
except:
    print("Invalid Input")
    exit(0)

res=sol(noOfParticipants,totalTime,info)
print(res)