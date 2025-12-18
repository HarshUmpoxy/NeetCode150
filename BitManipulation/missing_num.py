# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

#############################################################################################################

# The main idea is that we initialize a variable res with n (len(nums)), now we iterate through the array and for each element we perform XOR operation with res and the element
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result^=i^nums[i]
        return result

# The main point to catch is that during the iteration, 'i' only goes from [0 - n-1] so we have initialized 'result' with n (len(nums))
# This ensures effectively that we are XORing all the numbers from [0 - n] n included with elements of nums (0-n with anyone missing) and the missing number will be the result