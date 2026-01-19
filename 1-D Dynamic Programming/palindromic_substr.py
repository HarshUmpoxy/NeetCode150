# Just a downward shift of Longest Palindromic Substr

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[False]*(n) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j] and (dp[i+1][j-1] or j-i<=2):
                    dp[i][j]=True
                    ans = ans + 1
        
        return ans