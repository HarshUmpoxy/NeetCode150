# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans, curr = -100000, 0
        for i in nums:
            curr = curr+i
            ans = max(ans, curr)
            if curr < 0:
                curr = 0
        return ans

# Time Complexity: O(N)
# Space Complexity: O(1)

###################################################################################################

# Dynamic Programming
# dfs(i, flag) -> i is the current index, flag indicates whether a subarray is already in progress.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [[None] * 2 for _ in range(len(nums) + 1)]

        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else -1e6
            if memo[i][flag] is not None:
                return memo[i][flag]
            if flag:
                memo[i][flag] = max(0, nums[i] + dfs(i + 1, True))
            else:
                memo[i][flag] = max(dfs(i + 1, False),
                                    nums[i] + dfs(i + 1, True))
            return memo[i][flag]

        return dfs(0, False)

# Time Complexity: O(N)
# Space Complexity: O(N)