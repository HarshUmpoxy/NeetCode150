# Solution-1
# if dp[i][j] is True, it means the substring s[i:j+1] is a palindrome
# Using this, we intend to find out dp[i+1][j-1] first before going to dp[i][j]
# This way we can save computation and check answer for all substrs (O(N^2))

# Iterate in a special way where i decreases and j increases
# i from n-1 to 0
# j from i to n-1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)
        dp = [[False]*(n) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j] and (dp[i+1][j-1] or j-i<=2):
                    dp[i][j]=True
                    if resLen < (j-i+1):
                        resLen = j-i+1
                        resIdx = i
        
        return s[resIdx: resIdx+resLen]