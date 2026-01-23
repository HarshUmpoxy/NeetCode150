import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dist = x*x + y*y  # squared distance (no sqrt)
            heapq.heappush(pq, (dist, [x, y]))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(pq)[1])

        return result
