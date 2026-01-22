class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        # Building adjacency list and indegree array
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        # building the queue with nodes having indegree 0
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        # processing the queue and filling the output array
        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []
        return output[::-1]