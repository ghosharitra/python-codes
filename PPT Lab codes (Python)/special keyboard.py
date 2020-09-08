"""
Recursion Q4)
Imagine you have a special keyboard 
with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending 
it after what has already been printed. 
If you can only press the keyboard for N times 
(with the above four keys), write a program to 
produce maximum numbers of A's. 
That is to say, the input parameter is N 
(No. of keys that you can press), the output is M 
(No. of As that you can produce).

Input:
The first line of input contains an integer T denoting 
the number of test cases. 
The first line of each test case is N, 
N is the number of key.

Output:
Print maximum number of A's. Print -1, if N is greater 
than 75.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 75

Example:
Input:
2
3
7

Output:
3
9

Explanation:
Testcase 1:  We can at most get 3 A's on screen by 
pressing following key sequence.
A, A, A.
Testcase 2: We can at most get 9 A's on screen by 
pressing following key sequence.
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

"""
def sol(n):
    #print("n:",n)
    if(n in d):
        return d[n]

    if(n<=0):
        return 0,0

    
    compare=[]
    for i in range(3):
        if(i==0):
            letter,buffer=sol(n-1)
            letter+=1
            compare.append([letter,buffer])
        elif(i==1):
            letter,buffer=sol(n-1)
            letter=letter+buffer
            compare.append([letter,buffer])
        else:
            letter,buffer=sol(n-3)
            buffer=letter
            letter=letter*2
            compare.append([letter,buffer])

        compare.sort(key = lambda row: (row[0],row[1]),reverse=True)

    d[n]=(compare[0][0],compare[0][1])
    #print("n:",n,"letters:",compare[0][0],"buffer:",compare[0][1])
    return compare[0][0],compare[0][1]



d={}

for _ in range(int(input())):
    n=int(input())
    if(n>75):
        print(-1)
    else:
        res=sol(n)
        print(res[0])
        #print("dict:",d)