# Solution-1
# Recursion + Memoization
# dp[i][j] represents LIS starting from i, with previous chosen element. at j
# If j == -1, it means no element has been chosen yet, so we have right shifted the index j by 1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][j] represents LIS starting from i, with previous chosen element. at j
        dp = [[-1]*(n+1) for _ in range(n)]

        def solve(i, j):
            if i>=n:
                return 0
            if dp[i][j+1]!=-1:
                return dp[i][j+1]
            ans = solve(i+1, j)
            if j==-1 or nums[i]>nums[j]:
                ans = max(ans, 1+solve(i+1,i))
            dp[i][j+1]=ans
            return dp[i][j+1]

        return solve(0, -1)

# Solution-2
# Binary Search on the Array maintaining the LIS

from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS