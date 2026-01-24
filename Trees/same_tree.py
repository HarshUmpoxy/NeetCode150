# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def solve(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            left = solve(p.left, q.left)
            right = solve(p.right, q.right)
            # print(left, right)
            if left and right and p.val == q.val:
                return True
            return False
        
        return solve(p, q)