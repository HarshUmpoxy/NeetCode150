class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)

        def solve(nums, i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i] = max(nums[i]+solve(nums, i+2), solve(nums, i+1))
            return dp[i]
        return solve(nums, 0)