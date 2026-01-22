# Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
# If there are multiple answers, return the answer that occurs last in the input.

# Solution:
# This uses the "peel off leaves" idea (often called topological trimming).
# Even though the graph is undirected, we can still remove nodes with degree 1 repeatedly:

# Nodes with degree 1 cannot be inside a cycle (a cycle needs every node to have degree ≥ 2).
# So we push all degree-1 nodes into a queue and remove them.
# When we remove a node, its neighbor's degree decreases; that neighbor might become a new leaf (degree 1), so we remove it next.
# After this process finishes, the only nodes left with degree > 0 are exactly the cycle nodes.
# Finally, the redundant edge must be an edge whose both ends are still in the cycle.
# Because we need the last such edge in input order, we scan edges in reverse and return the first edge connecting two remaining cycle nodes.


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]==2: # The 2nd condition is imp because of eg. [1,5]
                return [u, v]
        return []