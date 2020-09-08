"""
Number Distancing
Problem Description
Consider 9 natural numbers arranged in a 3x3 matrix:
n11 n12 n13
n21 n22 n23
n31 n32 n33
Define numbers "in contact" with a given number to be those that appear closest to it on the same row, column or diagonally across:
Contacts of number n11: n12, n22 and n21
Contacts of number n12: n11, n21, n22, n23, n13
Contacts of number n13: n12, n22, n23
Contacts of number n21: n11, n12, n22, n32, n31
Contacts of number n22: n11, n12, n13, n23, n33, n32, n31, n21
Contacts of number n23: n13, n12, n22, n32, n33
Contacts of number n31: n21, n22, n32
Contacts of number n32: n31, n21, n22, n23, n33
Contacts of number n33: n32, n22, n23
The problem now is that numbers having a common factor (other than 1) should not be "in contact". In other words, a pair of numbers can remain neighbours only if their highest common factor is 1.
The following rules apply to enforce this "distancing":
1. The central number (n22) stays put.
2. The corner numbers (n11, n13, n33, n31) can move in the same row or column or diagonally away from the centre.
3. The numbers "on the walls" (n12, n23, n32, n21) can only move from the walls i.e. n21 can only move "left", n12 can only move "up", n23 can only move "right" and n32 can only move "down".
4. Each number should stay put as far as possible and the "distancing" operation should result in the least number of numbers ending up without any contacts.
5. After satisfying rule 4, if there are multiple options for the final matrix, then the "distancing" operation should result in the smallest (m x n matrix, including the intervening blank space elements, with the least possible value of m*n).
6. If, after satisfying all the rules above, there are multiple distancing options for a set of numbers, the largest number keeps to its original cell.
Constraints
1 <= Element of grid <= 100
Input
First line consists of 9 space separated integers denoting n11, n12, n13, .... n23, n33 respectively.
Output
Print the "contact" less numbers in ascending order of their value separated by space. Output "None" if there are no such numbers.
Time Limit
1
Examples
Example 1
Input
23 33 12 1 2 5 25 6 10
Output
10
Explanation
Initial configuration
23 33 12
1 2 5
25 6 10
The optimal distancing options result in the following possibility (space denoted by *):
23 33 * 12
1 2 5 *
25 * * *
* 6 * 10
10 ends up as the number without contacts.
Example 2
Input
1 2 3 4 5 6 7 8 9
Output
None
Explanation
Initial configuration:
1 2 3
4 5 6
7 8 9
The optimal distancing options result in the following 5x3 matrix (space denoted by *):
* 2 3
1 * *
4 5 6
7 * *
* 8 9
There is finally no number without a contact.
Example 3
Input
2 6 2 10 19 12 2 20 2
Output
2 2 2 2 10 12
Explanation
Initial Configuration:
Approach 1) Moving 6 and 20
Final Matrix
2 * 6 * 2
* * * * *
* 10 19 12 *
* * * * *
2 * 20 * 2
Approach 2) Moving 10 and 12
2 * * * 2
* * 6 * *
10 * 19 * 12
* * 20 * *
2 * * * 2
We prefer approach 2) and not 1) since the largest of all the elements (20) needs to be retained in it's original cell.


"""