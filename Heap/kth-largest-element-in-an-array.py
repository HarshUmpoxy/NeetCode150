class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [-i for i in nums]
        heapq.heapify(pq)
        for i in range(k-1):
            heapq.heappop(pq)
        return -pq[0]