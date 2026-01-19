# The Question demands us to partition the array into two equal sum subsets
# The target is (sum of array)/2 exactly without any remainder
# dp[i][target] represents if it is possible standing at index i to obtain the sum target from there
# If target == 0, it means we have successfully partitioned the array into two equal sum subsets

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]

            memo[i][target] = (dfs(i + 1, target) or
                               dfs(i + 1, target - nums[i]))
            return memo[i][target]

        return dfs(0, target)