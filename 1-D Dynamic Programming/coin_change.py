# Take or not take the current position, recursion takes care of the rest

class Solution:
    def solve(self, curr_ind, amount, coins, dp):
        if curr_ind <0 or amount < 0:
            return 1e9
        if amount == 0:
            return 0
        if dp[amount][curr_ind] != -1:
            return dp[amount][curr_ind]
        
        #skip
        ans1 = self.solve(curr_ind-1, amount, coins, dp)
        #take current
        ans2 = 1 + self.solve(curr_ind, amount-coins[curr_ind], coins, dp)

        dp[amount][curr_ind] = min(ans1, ans2)
        return dp[amount][curr_ind]
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        col = len(coins) + 1
        row = amount+1
        dp = [[-1]*col for _ in (range(row))]
        ans = self.solve(len(coins)-1, amount, coins, dp)
        if ans==1e9:
            ans=-1
        return ans