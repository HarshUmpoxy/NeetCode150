# The catch is to think about the last balloon to burst in a range
# This way we can divide the problem into two subproblems
# dp[i][j] = maxCoins in range (i, j)
# The base condition of recursion dp[i][j] = max of (nums[l - 1] * nums[i] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r))
# We add 1 at the start and end of the array to handle the edge cases


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)