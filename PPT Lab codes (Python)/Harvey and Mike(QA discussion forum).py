"""
ARRAY Q7)
Given a NxNxN grid. Harvey and Mike are playing a game. 
The rule of the game is simple. 
Each of them in their turn choses a cell 
and mark it with their initials. 
But the catch here is once a cell is marked 
they can't chose any of the adjacent(sharing a 
common face not the just the edge) cell to it. 
Since Harvey is senior he goes first. 
Both of them play optimally. 
The player with no move remaining loses the game. 
If harvey wins the game print “Harvey” 
otherwise print “Mike”.

Input :
The first line contains integer T, 
denoting number of test cases. 
Then T test cases follow. 
The first line of each test case contains an integer N, 
denoting the dimensions of the grid.

Output :
Print the answer of each test case in a new line.

Constraints :
1 <= T <= 100
1 <= N <= 1018

Example:
Input :
2
2
7

Output :
Mike
Harvey

Explanation:
Testcase 1: 2*2*2 grid they have 8 blocks, if Harvey marks any of the cell the then Mark has only three options left, and once Mike chooses any one of the three, then Harvey has no other option so mike wins.

"""

for i in range(t):
    n = int(input())
    n = n**3
    j = 0
    while n > 0:
        j = j + 1
        n = n - 5
    if j%2 == 0:
        print("Mike")
    else:
        print("Harvey")