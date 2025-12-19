# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#############################################################################################################

# The main idea is that we convert the number to string and reverse it
# For negative numbers, we reverse the string without the first character (the negative sign) by skipping it [1:] and then reverse it [::-1] and multiply by -1
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            res = int(str(x)[::-1])
        else:
            res = int(str(x)[1:][::-1])*-1
        
        if res > 2**31-1 or res < -2**31: #important : int 
        #ranges from [-2^31 - 2^31-1] as 
        #0 is included in positive half
            return 0
        
        return res
        