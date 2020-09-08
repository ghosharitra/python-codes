"""
Q12)
Given an array arr[] of N integers. 
Do the following operation n-1 times. 
For every Kth operation:

Right rotate the array clockwise by 1.
Delete the (n-k+1)th last element.
Now, find the element which is left at last.

Input:
The first line of input contains an integer T 
denoting the number of test cases. 
Then T test cases follows. 
Each test case contains two lines. 
The first line of each test case contains an integer N. 
Then in the next line are N space separated values 
of the array arr[].

Output:
For each test case in a new line print the required result.

Constraints:
1 <= T <= 110
1 <= N <= 106
1 <= A[i] <= 107

Example:
Input
2
4
1 2 3 4
6
1 2 3 4 5 6

Output:
2
3

Explanation:
Testcase 2: A = {1, 2, 3, 4, 5, 6}. 
Rotate the array clockwise i.e. after rotation 
the array A = {6, 1, 2, 3, 4, 5} and delete the last 
element that is {5} so A = {6, 1, 2, 3, 4}. 
Again rotate the array for the second time and deletes 
the second last element that is {2} so A = {4, 6, 1, 3}, 
doing these steps when he reaches 4th time, 
4th last element does not exists so he deletes 
1st element ie {1} so A={3, 6}. 
So continuing this procedure the last element in A is {3}, 
so outputp will be 3.


"""
#THIS WAS NOT MY LOGIC, GOT IT QA DISCUSSION FORUM


for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if(n==1):
        print(l[0])
        continue
    elif(n%2):
        ind = n-3
        ind = ind//4
        ind = 3+ind
        print(l[ind-1])
        continue
    else:
        ind = n-2
        ind = ind//4
        ind = 2+ind
        print(l[ind-1])
        continue