class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            result^=nums[i]
        return result

#############################################################################################################
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#############################################################################################################

# Using x^x=0, and x^0=x so all the numbers that appear twice will cancel out and the only number that will 
# remain is the one that appears once.