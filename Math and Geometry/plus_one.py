# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#####################################################################################################################

# The main idea is that we traverse the array from right to left and if the current digit is less than 9, we increment it by 1 and return the array.
# If the current digit is 9, we set it to 0 and continue.
# If we reach the leftmost digit and it is 9, we set it to 0 and return [1] + digits.

#####################################################################################################################

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # if we reach here, all digits were 9
        return [1] + digits
