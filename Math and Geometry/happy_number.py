# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

##############################################################################################################################

# if N == 1: return True [Happy Number]
# if N repeats itself (that means there's a cycle not ending in 1): return False [Not Happy Number]
# keep a record of N (in a seen set)
# update N to sum of square of digits

##############################################################################################################################

class Solution:
    def solve(self, n: int) -> int:
        ans = 0
        while n>0:
            last = n%10
            ans += (last**2)
            n//=10 #Note n=/=10 gives decimal values
        return ans

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            next = self.solve(n)
            # print(next) #Used to debug n//=10 instead of n/=10
            n = next
            if next == 1:
                return True
            if next in seen:
                return False
            seen.add(next)
        return True