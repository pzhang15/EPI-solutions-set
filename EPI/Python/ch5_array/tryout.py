'''
Your input is an array of integers, 
and you have to reorder its entries so that the even entries appear first. 
This is easy if you use O(n) space, where n is the length of the array.
However, you are required to solve it O(1) space`.
'''

'''
LC 75. Sort Colors
Suppose A = ⟨0, 1, 2, 0, 2, 1, 1⟩, and the pivot index is 3. 
Then A[3] = 0, so ⟨0, 0, 1, 2, 2, 1, 1⟩ is a valid partitioning. 
For the same array, if the pivot index is 2, then A[2] = 2, 
so the arrays ⟨0, 1, 0, 1, 1, 2, 2⟩ as well as ⟨0, 0, 1, 1, 1, 2, 2⟩ are valid partitionings.

Write a program that takes an array A and an index i into A, 
and rearranges the elements such that all elements less than A[i] (the “pivot”) appear first, 
followed by elements equal to the pivot, followed by elements greater than the pivot.
'''


'''
Write a program which takes as input an array of digits encoding a decimal number D 
and updates the array to represent the number D + 1. 
is (1,2,9) then you should update the array to (1,3,0). 
Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.
'''

'''
Certain applications require arbitrary precision arithmetic. 
One way to achieve this is to use arrays to represent integers, 
e.g., with one digit per array entry, with the most significant digit appearing first, 
and a negative leading digit denot¬ inganegativeinteger. 
For, example,(1,9,3,7,0,7,7,2,1)represents 193707721
        and (-7,6,1,8,3,8,2,5,7,2,8,7) represents-761838257287.
Write a program that takes two arrays representing integers, and returns an integer representing their product.
For example, since 193707721 X -761838257287 = -147573952589676412927, if the inputs are  (1,9,3,7,0,7,7,2,1} and (-7,6,1,8,3,8,2,5,7,2,8,7), 
your function should return (-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7).
'''

'''
In a particular board game, a player has to try to advance through a sequence of positions. 
Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move. 
You begin at the first position,and win by getting to the last position. For example,letA = {3,3,1,0,2,0,1} represent the board game, i.e., 
the ith entry in A is the maximum we can advance from i. 
Then the game can be won by the following sequence of advances through A: take 1 step from A[0] to A[1], then 3 steps from A[l] to A[4], then 2 steps from A[4] to A[6], which is the last position. Note that A[0] = 3 > 1, A[l] = 3 > 3, and A[4] = 2 > 2, so all moves are valid. 
If A instead was (3, 2, 0, 0, 2, 0,1), it would not possible to advance past position 3, so the game cannot be won.
Write a program which takes an array of n integers, 



where A[i] denotes the maximum you can advance from index i, 
and returns whether it is possible to advance to the last index starting from the beginning of the array.
'''

'''
Write a program which takes as input a sorted array
Updates it so that all duplicates have been removed 
and the remaining elements have been shifted left to fill the emptied indices. 
Return the number of valid elements. 
Many languages have library functions for performing this operation—you cannot use these functions.
Hint: There is an 0(n) time and 0(1) space solution.
'''