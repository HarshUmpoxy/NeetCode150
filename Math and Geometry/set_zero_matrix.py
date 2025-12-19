# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

#############################################################################################################

# The main idea is that we first store the position of the 0s in a list and then set the entire row and column to 0s.
# v: list(tuple(int, int)) is an important concept, '(' are used for tuple and not '{'
# To iterate over a tuple, use  for x, y in v unlike for i in range(v): v[i][0], v[i][1] is bit overhead but works

#############################################################################################################

class Solution:
    def fix(self, matrix, i, j):
        # Row is i, Col is j
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            matrix[r][j]=0
        for c in range(col):
            matrix[i][c]=0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        v: list(tuple(int, int)) = []
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    v.append((i, j))
        
        for i in range(len(v)):
            self.fix(matrix, v[i][0], v[i][1])
        