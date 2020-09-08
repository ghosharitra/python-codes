"""
Tahir & Mamta are woking in a project in TCS. Tahir being a issue solver came up with an  interesting problem for his best friend Mamta. Problem consisting of a string of length N & consisting only small case alphabets. 
It will be followed by given  Q queries, in which every query will have  an integer P (1<=P<=N) denoting  a position within the string. 
Mamta's objective  is to ﬁnd the alphabet present at that location & determine the no. of occurrence of same alphabet preceding the given location P . Mamta is very very  busy with her oﬃce work. Hence , Mamta asking  for help.
Constraints
1 <= N <= 500000 
 S consisting of small case alphabets 
1 <= Q <= 10000
1 <= P <= N
Input Format
First line : an integer N, describing the length of string. 
Second line : string S itself made up of small case alphabets only ('a' - 'z').
Third line : an integer Q denoting no.  of queries that will be asked.
Next Q lines :  An integer P (1 <= P <= N) for which you have  to ﬁnd the no. of occurrence of character present at the Pth location preceeding P . 
Output 
Integer describing the Ans on single line.
Explanation 
Input
9
abacsddaa
2
9
3
 
Output
3
1
 
Explanation
Here Q is equal to 2 
For P=9, character at Ninth  location is "a". No. of occurrences of 'a' before P i.e., 9 is 3 .
Similarly for P=3, Third character is 'a'. No.of occurrences of 'a' before P. i.e., 3 is 1.


"""
def sol(string,n,queries,t):
    res=[]
    for i in range(t):
        q=queries[i]
        ch=string[q]
        count=0
        for i in range(q):
            if string[i]==ch:
                count+=1
        res.append(count)
    return res




try:
    n=int(input("enter length: "))
    string=input("enter string: ").lower()[:n]
    if len(string)!=n:
        raise Exception
    t=int(input("cases: "))
    queries=[]
    for i in range(t):
        val=int(input("q: "))
        if val>n:
            raise Exception
        queries.append(val-1)
except:
    print("Invalid Input")
    exit(0)

res=sol(string,n,queries,t)

for i in range(t):
    print(res[i])