# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. 
# In other words, if you are at index i, you can jump to any index (i + j) where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach index n - 1. 
# The test cases are generated such that you can reach index n - 1.

class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return 1000000

            res = 1000000
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            memo[i] = res
            return res

        return dfs(0)

# Solution 2:
# This problem asks for the minimum number of jumps needed to reach the last index.

# We can think of this problem as moving level by level, similar to Breadth First Search (BFS):

# each “level” represents all positions we can reach using the same number of jumps
# from those positions, we compute how far we can reach in one more jump
# Instead of explicitly using a queue, we use a greedy window:

# [l, r] represents the range of indices reachable with the current number of jumps
# from this range, we find the farthest index we can reach in the next jump
# Once we finish scanning the current range, we move to the next range and increase the jump count.

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res