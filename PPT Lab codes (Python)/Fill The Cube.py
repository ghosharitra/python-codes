"""
Problem Description
A company manufactures walls which can be directly implanted at the site. The company uses small square bricks of material C and material D which have similar looks but have huge difference in quality. The company manufactures walls of square shapes only to optimize their costs.

A novice employee created a square wall using bricks of material C and D. However, the client had asked the wall to be made of only high-quality material - material C.

To solve this problem, they will place the wall in a special furnace and heat it such that the material D melts and only material C remains. Material C brick will move down due to gravity if a material D brick below it melts. The new empty space created will be filled by new material C square walls. They also want to use biggest possible C square wall while building the final wall. For this they will position the wall in the furnace in an optimal way i.e. rotate by 90-degrees any number of times, if required, such that the biggest space possible for new material C wall is created. No rotations are possible when the furnace starts heating.

Given the structure of the original wall created by the novice employee, you need to find out the size of the new C square wall which can be fitted in the final wall which will be delivered to the client.

Constraints
1 < N < 100

Input
First Line will provide the size of the original wall N.

Next N lines will provide the type of material (C and D) used for each brick by the novice employee.

Output
Size of the biggest possible C square wall which can be fitted in the final wall.

Time Limit
1


Examples
Example 1

Input

4
C D C D
C C D C
D D D D
C D D D

Output

3

Explanation

If the wall is placed with its left side at the bottom, space for a new C wall of size 2x2 can be created. This can be visualized as follows

D C D D

C D D D

D C D D

C C D C

The melted bricks can be visualized as follows

- - - -

- C - -

C C - -

C C - C

Hence, the maximum wall size that can be replaced is 2x2.

If the wall is placed as it is with its original bottom side at the bottom, space for a new C wall of size 3x3 can be created. Post melting, this can be visualized as follows.

- - - -

C - - -

C - - -

C C C C

Hence, the maximum wall size that can be replaced is 3x3 in this approach.

Since no rotations followed by heating is going to a yield a space greater than 3x3, the output is 3.

Example 2

Input

7
C D D C D D D
C D D C D D D
D D D D D D C
D C D C D D D
D D D C D C D
C D D C D C C
C D C D C C C

Output

5

Explanation

If the wall is placed with its left side at the bottom, a space for new C wall of size 5x5 can be created. This can be visualized as follows

D D C D D C C
D D D D C C C
D D D D D D C
C C D C C C D
D D D D D D C
D D D C D D D
C C D D D C C

When this orientation of the wall is heated, a space for new C wall of size 5x5 is created after the D bricks melt

_ _ _ _ _ _ _
_ _ _ _ _ _ _
_ _ _ _ _ _ C
_ _ _ _ _ C C
_ _ _ _ _ C C
C C _ C C C C
C C C C C C C

Whereas, if the rotation was not done, the wall formed after the D bricks melt will be as follows

_ _ _ _ _ _ _
_ _ _ _ _ _ _
_ _ _ C _ _ _
C _ _ C _ _ _
C _ _ C _ _ C
C _ _ C _ C C
C C C C C C C

When this orientation of the wall is heated, a space for new C wall of size 3x3 only is created after the D bricks melt

Hence rotation is important and correct answer is 5x5

Since no rotations followed by heating is going to a yield a space greater than 5x5, the output is 5.




Input:
100
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D
D D C D D D D C D D D D C D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D D D D D D D D D D D                                                        
D D C D D D D C D D D D C D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D D D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D C D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D C D D C D D D D D D D D D C D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D C D C D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D C D C D 
D D D D D D D D D D D D D D D C D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D

Output:
89





"""
def disp(mat,n):
    print()
    
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=" ")
        print()
    



def zeroSq(mat,n):
    res=0
    
    colcount=[]
    for i in range(n):
        count=0
        for j in range(n-1,-1,-1):
            if(mat[j][i]==0):
                count+=1
            else:
                break
        colcount.append(count)
    
    print(colcount)
    
    for i in range(n):
        if i+colcount[i]<=n and colcount[i]>res:
            for j in range(colcount[i]):
                
                if colcount[i+j]<colcount[i]:
                    break
            else:
                if res<colcount[i]:
                    res=colcount[i]

        if i-colcount[i] + 1 >=0 and colcount[i]>res:
            for j in range(colcount[i]):
                if colcount[i-j]<colcount[i]:
                    break
            else:
                if res<colcount[i]:
                    res=colcount[i]

    print("res:",res)
    return res





def melt(matrix,n):
    for i in range(n):
        pos=0
        for j in range(n):
            if(matrix[j][i]=="D"):
                matrix[j][i]=0
            elif(matrix[j][i]=="C"):
                if pos!=j:
                    matrix[j][i]=0
                    matrix[pos][i]="C"
                pos+=1
    
    disp(matrix,n)



def rotate(matrix,m):
    n=m
    c=0
    while(n>1):
        for i in range(n-1):
            t=matrix[c][c+i]
            matrix[c][c+i]=matrix[m-c-1 -i][c]
            matrix[m-c-1 -i][c]=matrix[m-c-1][m-c-1 -i]
            matrix[m-c-1][m-c-1 -i]=matrix[c+i][m-c-1]
            matrix[c+i][m-c-1]=t
        c=c+1 
        n=n-2


def opr(matrix,n):
    mat= [[j for j in i] for i in matrix]
    
    melt(mat,n)
    x1=zeroSq(mat,n)

    rotate(matrix,n)
    disp(matrix,n)

    melt(matrix,n)
    x2=zeroSq(matrix,n)

    return max(x1,x2)





matrix=[]
try:
    n=int(input())
    if(n>100 or n<=1):
        raise Exception
    

    for i in range(n):
        temp=input().split()
        if len(temp)!=n:
            raise Exception
        for i in temp:
            if i!='D' and i!='C':
                raise Exception
        
        matrix.append(temp)
except:
    exit(0)


res=opr(matrix, n)
print(res)





