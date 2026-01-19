# Intuition is easy, the key is IMPLEMENTATION

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s):1}
        def solve(i):
            if i in dp:
                return dp[i]
            
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    if solve(i+len(w)):
                        dp[i]=True
                        return True
            dp[i]=False
            return False
        return solve(0)