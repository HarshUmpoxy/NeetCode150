# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and 
# the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have
# any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

##########################################################################################################################################################

# Three cases observed, :
# newInterval is to the left of intervals -> no overlap, append and return
# newInterval is to the right of intervals -> no overlap, append only
# newInterval is overlapping with intervals -> merge and let it continue

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        for i in range(n):
            if intervals[i][1] < newInterval[0]: # Case 2
                print("Here1")
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]: # Case 1
                print("Here2")
                res.append(newInterval)
                return res + intervals[i:]
            else: # Case 3
                print("Here")
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res