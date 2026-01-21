# Fun problem, as we might end up with a cycle in the graph
# So we need to use a visited set to keep track of the nodes we have already visited (oldToNew)
# Also, we need to return the new node, not the old node in base case

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        if len(node.neighbors) == 0:
            return Node(node.val)
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node] #return the oldToNew[node], imp for new ref
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None