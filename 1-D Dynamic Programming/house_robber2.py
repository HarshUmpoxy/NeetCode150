# The Single Most Common observation build on Top of the Previous Question
# The first and the last house can't be chosen together anymore
# So we can break the problem into two subproblems
# 1. Robbing the houses from the first to the second last
# 2. Robbing the houses from the second to the last
# And then take the maximum of the two

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def solve(nums, i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i] = max(nums[i]+solve(nums, i+2), solve(nums, i+1))
            return dp[i]
        
        dp = [-1]*(n+1)
        first = solve(nums[:-1], 0)
        
        dp = [-1]*(n+1)
        second = solve(nums[1:], 0)
        
        return max(first, second)

# The First Implementation is more Intuitive and Common
# However, we can use a Flag that shows whether we have chosen the first house or not and tweak the conditions accordingly
# The edge case is when there is only one house, which is taken care of by the max function (nums[0])
# The code fails because the first and the last element is same and both the solve f(x)'s will return 0

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*2 for _ in range(n+1)]
        def solve(i, flag):
            if i>=n or flag and i==n-1:
                return 0
            if dp[i][flag]!=-1:
                return dp[i][flag]
            dp[i][flag] = max(solve(i+1, flag), nums[i]+solve(i+2, flag))
            return dp[i][flag]
        return max(max(nums[0],solve(0, True)), solve(1, False))