from typing import List, Optional

# class TreeNode:
#     def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preLow: int, preHigh: int, inLow: int, inHigh: int) -> Optional[TreeNode]:
            if preLow > preHigh or inLow > inHigh:
                return None

            root_val = preorder[preLow]
            root = TreeNode(root_val)

            # Find root index in inorder
            inIndex = inLow
            while inorder[inIndex] != root_val:
                inIndex += 1

            countLeft = inIndex - inLow

            root.left = build(
                preLow + 1,
                preLow + countLeft,
                inLow,
                inIndex - 1
            )

            root.right = build(
                preLow + countLeft + 1,
                preHigh,
                inIndex + 1,
                inHigh
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)