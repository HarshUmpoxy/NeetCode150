# Solution -1 
# Not Recommended for interviews as we are yet to use the binary search property

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node, target, path):
            if not node:
                return False

            # add current node to path
            path.append(node)

            if node == target:
                return True

            if dfs(node.left, target, path) or dfs(node.right, target, path):
                return True

            # backtrack if not on the correct path
            path.pop()
            return False

        path_p = []
        path_q = []

        dfs(root, p, path_p)
        dfs(root, q, path_q)

        # find last common node
        lca = None
        i = 0
        while i < len(path_p) and i < len(path_q):
            if path_p[i] == path_q[i]:
                lca = path_p[i]
            else:
                break
            i += 1

        return lca


# Solution - 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
     