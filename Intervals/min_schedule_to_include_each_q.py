# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti
# and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, 
# or more formally righti - lefti + 1.

# You are also given an integer array queries. The answer to the jth query is the size of the smallest
# interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

# Return an array containing the answers to the queries.

# This solution uses an Offline Query approach with a Sweep Line. 
# By sorting both intervals and queries, we can process the number line in a single pass. 
# We use a Min-Heap to maintain the set of currently active intervals, ordered by size. 
# We use a Lazy Removal strategy on the heap—only popping the top element when it's no longer valid—
# which keeps the logic efficient.

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals); m = len(queries)
        res = [-1]*m
        idx = list(range(m))

        intervals.sort()
        idx.sort(key=lambda x: queries[x])
        pq = []

        i=0
        for j in range(m):
            id = idx[j]; pos = queries[id]
            while i<n and intervals[i][0]<=pos :
                heapq.heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1
            while pq and pq[0][1] < pos:
                # pq.pop() -> breaks the heap in Python, wrong to use
                heapq.heappop(pq)
            if pq:
                res[id] = pq[0][0]
        
        return res