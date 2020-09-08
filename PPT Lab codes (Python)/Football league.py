"""
Football League Table Statement : All major football leagues have big league tables. Whenever a new match is played, the league table is updated to show the current rankings (based on Scores, Goals For (GF), Goals Against (GA)). Given the results of a few matches among teams, write a program to print all the names of the teams in ascending order (Leader at the top and Laggard at the bottom) based on their rankings.

Rules:
A win results in 2 points, a draw results in 1 point an
d a loss is worth 0 points. The team with the most goals in a match wins the match. Goal Difference (GD) is calculated as Goals For (GF) Goals Against (GA). Teams can play a maximum of two matches against each other Home and Away matches respectively.

The ranking is decided as follows: Team with maximum points is ranked 1 and minimum points is placed last Ties are broken as follows Teams with same points are ranked according to Goal Difference(GD).

If Goal Difference(GD) is the same, the team with higher Goals For is ranked ahead

If GF is same, the teams should be at the same rank but they should be printed in case-insensitive alphabetic according to the team names. More than 2 matches of same teams, should be considered as Invalid Input.

A team can’t play matches against itself, hence if team names are same for a given match, it should be considered Invalid Input

Input Format:
First line of input will contain number of teams (N) Second line contains names of the teams (Na) delimited by a whitespace character Third line contains number of matches (M) for which results are available Next M lines contain a match information tuple {T1 T2 S1 S2}, where tuple is comprised of the following information

T1 Name of the first team
T2 Name of the second team
S1 Goals scored by the first team
S2 Goals scored by the second team
Output Format:
Team names in order of their rankings, one team per line OR Print “Invalid Input” where appropriate.

Constraints:

0< N <=10,000 0<=S1,S2

Example:
Consider 5 teams Spain, England, France, Italy and Germany with the following fixtures:

Match 1: Spain vs. England (2-0) (Spain gets 2 points, England gets 0)
Match 2: England vs. France (1-1) (England gets 1 point, France gets 1)
Match 3: Spain vs. France (0-2) (Spain gets 0 points, France gets 2)
Table 1. Points Table after 3 matches

Team Name	Matches Played	Goals for	Goals Against	Goal Difference	Points	Ranking
Spain	2	3	2	1	2	2
England	2	1	4	-3	1	3
France	2	3	1	2	3	1
Italy	0	0	0	0	0	4
Germany	0	0	0	0	0	4
Since, Italy and Germany are tied for points, goals difference is checked. Both have same, so, Goals For is checked. Since both are same. Germany and Italy share the 4th rank. Since Germany appears alphabetically before Italy, Germany should be printed before Italy. Then the final result is: France Spain England Germany Italy



Sample Input 1:
5
Spain England France Italy Germany
3
Spain England 3 0
England France 1 1
Spain France 0 2


Sample Output 1:
France
Spain
England
Germany
Italy


Sample Input 2:
5
Spain England France Italy Germany
3
Spain England 3 0
England France 1 1
Spain Spain 0 2


Sample Output 2:
Invalid Input

"""

nteams=int(input())
teams={}
x=input().split()[:nteams]
for i in x:
    teams[i]=[0,0,0,0]

line=int(input())

for i in range(line):
    
    s=input().split()  
    team1=s[0]
    team2=s[1]
    if(team1==team2):
        print("Invalid Input")
        exit(0)


    temp1=teams[team1]
    temp2=teams[team2]
    temp1[0]+=1
    temp2[0]+=1
    if temp1[0]>2 or temp2[0]>2:
        print("Invalid Input")
        exit(0)

    temp1[1]+=int(s[2])
    temp1[2]+=int(s[3])
    
    temp2[1]+=int(s[3])
    temp2[2]+=int(s[2])

    if s[2]>s[3]:
        temp1[3]+=2
    elif s[2]==s[3]:
        temp1[3]+=1
        temp2[3]+=1
    else:
        temp2[3]+=2


    teams[team1]=temp1
    teams[team2]=temp2


info=[]


for i in teams.keys():
    x=teams[i]
    temp=[ i, x[1], x[2], x[3], x[1]-x[2]  ] 
    info.append(temp)



info.sort(key = lambda row: (row[0].lower() )) 

info.sort(key = lambda row: (row[3],row[4],row[1]),reverse=True) 



print()
for i in info:
    print(i)