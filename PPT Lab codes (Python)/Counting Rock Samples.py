"""
Juan Marquinho could be a man of science i.e  geologist and he have to count rock samples in order to send it to a chemical laboratory. 

Juan Marquinho  has a problem : The laboratory only accepts rock samples by a range of its size in ppm ( parts per million ) .

Geologist Juan Marquinho  , he receives the rock samples one by one and geologist Juan Marquinho classifies the rock samples according to the range of the laboratory. This process is very difficult because the no. of rock samples may be in millions. Geologist Juan Marquinho needs your help, your task is develop a program to get the no. of rocks in each of the ranges accepted by the laboratory. 

Input Format
An positive integer S (the number of rock samples) separated by a blank space, and a positive integer R (the number of ranges of the laboratory); a listing of sizes of S samples (in ppm), as positive integers separated by space R lines where the ith line containing two positive integers, space separated, indicating the minimum size and maximum size severally of the ith range.

Output Format
R lines 
where as the ith line containing a single non-negative integer describe the no. of the samples 
Constraints
10 ≤ S ≤ 10000 
1 ≤ R ≤ 1000000 
1≤ size of each sample in ppm ≤ 1000
Sample Input and Output 
Example 1
Input
10 2 
 345 604 321 433 704 470 808 718 517 811 
300 350 
400 700
Output
2 4

Explanation:
There are Ten samples (S) & Two ranges ( R ). The samples are  345 604 321 433 704 470 808 718 517 811 . The ranges are 300-350 & 400-700. There are Two samples in the first range (345 & 321) & Four samples in the 2nd range (604, 433, 470, 517). Therefore the two lines of the o/p are 2 and 4

Example 2
Input
20 3 
921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195 
1 100 
50 600 
1 1000
Output
1 12 20

Explanation:
There are 20 samples & 3 ranges. The samples are 921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195 . The ranges are 1-100, 50-600 & 1-1000. 
Note : the ranges are overlapping. 
The no. of samples in each of the 3 ranges are 1, 12 and 20 respectively. Therefore  the 3 lines of the o/p are 1, 12 and 20.

"""
def sol(noOfRock,rockSeries,noOfRange,ranges):
    res=[0]*noOfRange
    for i in range(noOfRock):
        for j in range(noOfRange):
            if(ranges[j][0]<=rockSeries[i] and rockSeries[i]<=ranges[j][1] ):
                res[j]+=1
    return res


try:
    noOfRock,noOfRange=map(int,input().split())
    rockSeries=list(map(int,input().split()))
    if(len(rockSeries)==0):
            raise Exception
    ranges=[]
    for i in range(noOfRange):
        temp=list(map(int,input().split()))
        if(len(temp)==0):
            raise Exception
        ranges.append(temp)
    
except:
    print("Invalid Input")
    exit(0)

res=sol(noOfRock,rockSeries,noOfRange,ranges)
for r in res:
    print(r,end=" ") 

