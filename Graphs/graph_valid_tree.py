# A graph is a valid tree if:

# It has no cycles
# It is fully connected
# Using DFS, we can detect cycles by checking if we visit a node again from a path other than its parent.
# Also, a tree with n nodes must have exactly n - 1 edges — otherwise it’s invalid.



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
