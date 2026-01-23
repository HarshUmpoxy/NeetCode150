# Dijkstra Algorithm - can't use simple dfs as there is no garantee that the current path is the shortest path
# Use min heap to always process the shortest path first
# Use dist array to store the shortest distance to each node
# Use pq to store the shortest distance to each node
# If the current distance is greater than the stored distance, continue
# Go to each connected node and check if we can optimize further
# Return the maximum distance from the source to any node

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        dist = {i: float("inf") for i in range(1,n+1)}
        dist[k] = 0

        pq = [(0,k)] # time, node

        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]: # dist[node] can't be optimized further
                continue

            for nei,wei in graph[node]: # go to each connected node and check if we can optimize further
                if wei + time < dist[nei]:
                    dist[nei] = wei + time
                    heapq.heappush(pq, (dist[nei], nei))
                
        ans = max(dist.values())
        return ans if ans < float('inf') else -1