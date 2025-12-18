# Given a positive integer n, write a function that returns the number of set bits in its binary representation 
# (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        wt = 0
        while n:
            n&=n-1
            wt+=1
        return wt

#############################################################################################################
