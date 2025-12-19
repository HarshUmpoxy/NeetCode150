# Given an m x n matrix, return all elements of the matrix in spiral order.

#############################################################################################################

# We use 4 pointers to keep track of the left, right, top, and bottom boundaries of the matrix.
# Also, the use of range function is important to note here. (range(left, right+1) or range(bottom, top-1, -1))
# Update the pointers after each iteration.
# Have a check on the conditions to avoid infinite loop. (top<=bottom and left<=right)

#############################################################################################################

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        ans = []
        left = 0; right = col-1; top =0; bottom = row-1
        while left<=right and top<=bottom:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans