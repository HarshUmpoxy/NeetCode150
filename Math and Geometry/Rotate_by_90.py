# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#############################################################################################################

# The main idea is that we first transpose the matrix and then reverse each row
# Time complexity: O(n^2)
# Space complexity: O(1)

#############################################################################################################

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # Transpose the matrix
        
        for r in range(row):
            matrix[r].reverse() # Reverse each row


# 90 = transpose + reverse row
# 180 = reverse row + reverse column
# 270 = transpose + reverse column
# Reverses the order of rows (Flip Vertically)
# Column 0 becomes the same column but read from bottom to top
# WAY 1 in Python
# matrix.reverse() 
# WAY 2
# top = 0
# bottom = len(matrix) - 1
# while top < bottom:
#     # Swap the entire rows
#     matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
#     top += 1
#     bottom -= 1