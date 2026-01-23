class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max-heap by negating values
        pq = [-s for s in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            s1 = -heapq.heappop(pq)  # largest
            s2 = -heapq.heappop(pq)  # second largest

            if s1 != s2:
                heapq.heappush(pq, -(s1 - s2))

        return -pq[0] if pq else 0