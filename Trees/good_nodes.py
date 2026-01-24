# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, maxTillNow):
            temp = 0
            if not root:
                return 0

            if root.val >= maxTillNow:
                temp +=1
            maxTillNow = max(maxTillNow, root.val)
            left = dfs(root.left, maxTillNow)
            right = dfs(root.right, maxTillNow)
            temp += left + right
            return temp
        
        return dfs(root, float("-inf"))