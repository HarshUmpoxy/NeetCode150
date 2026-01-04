# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals
# non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# Logic is to sort based on the end points rather than the start points
# Syntax for sorting in Python intervals.sort(key=lambda x: (primary key, secondary key))
# eg. intervals.sort(key=lambda x: (x[1], -x[0]))

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 1. Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        curr_end = intervals[0][1]

        # 2. Iterate through intervals
        for i in range(1, len(intervals)):
            # Overlap case
            if intervals[i][0] < curr_end:
                removals += 1
            else:
                # No overlap, update curr_end
                curr_end = intervals[i][1]

        return removals
