# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.

# Logic and intuition is derived from insert_interval.py

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)
        intervals.sort()
        curr = intervals[0]

        for i in range(1,n):
            #curr and the now do not merge
            #curr is left of now, so append curr and update curr with now
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            #curr can never be right of now (the start of curr and start of now)
            #means they merge now, update curr with the merge of two and proceed
            else:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
        #append curr in the result
        res.append(curr)
        return res