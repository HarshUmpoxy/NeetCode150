# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root):  # returns (minVal, maxVal, isValid)
            if not root:
                return (float("inf"), float("-inf"), True) # reverse the return -> BRAVO MOMENT

            minLeft, maxLeft, ans1 = solve(root.left)
            minRight, maxRight, ans2 = solve(root.right)

            if ans1 and ans2 and maxLeft < root.val < minRight:
                return (
                    min(root.val, minLeft),
                    max(root.val, maxRight),
                    True
                )

            # return (float("inf"), float("-inf"), False)
            return (5, -5, False) # Trying to prove it doesn't matter
        return solve(root)[2]
