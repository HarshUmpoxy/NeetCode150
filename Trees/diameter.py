# At every node, the diameter can be:

# Completely in the left subtree

# Completely in the right subtree

# Passing through the current node

# So recursively compute left info, right info, and combine them.

# Why we shifted from your intuition to the optimal form
# Step 1: What information does a parent actually need?
# From a child, the parent only needs one thing to do its job:
# The maximum height of that subtree
# That’s it.

# The parent:
# does not need the child’s diameter to compute its own height
# can compute “diameter through me” using just left & right heights
# So returning diameter upward is extra information.

# Step 2: Diameter does not help higher nodes
# A diameter found in a subtree:
# is complete

# will never be extended by ancestors

# So once a diameter is computed, it only needs to be:

# remembered, not passed upward

# This is the key insight.

# Think of diameter as a global candidate, not a building block.

# Step 3: Separate responsibilities

# Your intuition mixes two responsibilities:

# computing height (used by parent)

# computing diameter (used globally)

# The optimal solution separates them:

# Task	Direction
# Height	flows upward
# Diameter	accumulated globally

# Once you see this separation, the simplification becomes obvious.

# Why the optimal version is strictly better

# No redundant returns

# Less mental overhead

# Clearer invariants:

# height(node) returns height

# diameter always stores best seen so far

# Same correctness. Same complexity. Cleaner logic.

# Final mental model (the “aha”)

# Height is what parents need.
# Diameter is what we care about globally.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            # update diameter Globally
            self.diameter = max(self.diameter, left + right)
            
            # return height
            return 1 + max(left, right)
        
        height(root)
        return self.diameter
