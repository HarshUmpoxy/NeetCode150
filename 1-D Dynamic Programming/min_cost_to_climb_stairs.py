class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)

        def solve(cost, i, n):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            ans = min(cost[i]+solve(cost, i+1, n), cost[i]+solve(cost, i+2, n))
            dp[i] = ans
            return dp[i]
        return min(solve(cost, 0, n), solve(cost, 1, n))