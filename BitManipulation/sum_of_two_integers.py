# Given two integers a and b, return the sum of the two integers without using the + operator.

#############################################################################################################

# The main idea is that :
# 1. When we have no carry, we can add easily using a^b
# 2. When we have a carry (a&b), we need to shift it left by 1 ((a&b)<<1) and add it to a
# 3. We repeat the process until there is no carry
# 4. We use a mask to handle overflow in python
# 5. We handle negative numbers using the mask

#############################################################################################################

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # mask to handle overflow in python
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF

        while b != 0:
            # carry
            carry = (a & b) & MASK
            # sum without carry
            a = (a ^ b) & MASK
            # shift carry left by 1
            b = (carry << 1) & MASK

        # handle negative numbers
        return a if a <= MAX else ~(a ^ MASK)
