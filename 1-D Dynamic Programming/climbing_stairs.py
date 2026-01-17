class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def solve(i, n):
            if i>n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            if i==n:
                return 1
            dp[i]=solve(i+1, n)+solve(i+2,n)
            return dp[i]
        return solve(0, n)