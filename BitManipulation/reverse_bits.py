# Reverse bits of a given 32 bits unsigned integer.

#############################################################################################################

# The main ideation is that we initialize a variable result with zero, now we iterate from rightmost bit of n
# Using (n&1) and we get the rightmost bit of n, then we left shift result by 1 (result<<1) and add the rightmost bit of n
# Then we right shift n by 1 (n>>1) and repeat the process until n becomes zero
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res= (res<<1) | (n&1)
            n>>=1
        return res