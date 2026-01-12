# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Using Dynamic Programming - O(N^2) and O(N)
# The main idea is to make a solve(i) function that returns true if we can reach the last index from index i.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        n = len(nums)
        def solve(i):
            if i == n-1:
                return True
            if i in dp:
                return dp[i]
            if nums[i]==0:
                return False
            end = min(n, i+1+nums[i])
            for j in range(i+1, end):
                if solve(j):
                    dp[j]=True
                    return dp[j]
            dp[j]=False
            return dp[j]
        return solve(0)

# Other insightful solutions

# We want to check if we can reach the last index starting from index 0.

# Instead of trying all possible jumps, we can think about the problem in reverse:

# ask which positions can eventually reach the end
# then move backward to see if earlier positions can reach those positions

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

# The Best Intuition Found so Far:

# Imagine you have a car, and you have some distance to travel (the length of the array). 
# This car has some amount of gasoline, and as long as it has gasoline, 
# it can keep traveling on this road (the array). Every time we move up one element in the array, 
# we subtract one unit of gasoline. However, every time we find an amount of gasoline that is 
# greater than our current amount, we "gas up" our car by replacing our current amount of gasoline 
# with this new amount. We keep repeating this process until we either run out of gasoline (and return false), 
# or we reach the end with just enough gasoline (or more to spare), in which case we return true.
# Note: We can let our gas tank get to zero as long as we are able to gas up at that immediate location 
# (element in the array) that our car is currently at.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True