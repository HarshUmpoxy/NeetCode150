class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        # If you have already successfully decoded the entire string
        # That counts as one valid decoding
        # Not zero, not multiple — exactly one complete path
        # If it were 0, then every decoding would fail, because every valid decoding eventually reaches the end.

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)