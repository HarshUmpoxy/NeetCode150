# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

# Classic case of divide and conquer. Depending on the sign of n, we either return 1 or 1/x.
# Also even odd cases are handled by the base cases.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x = 1/x
            n = abs(n)
        if n==1:
            return x
        if n%2 == 1:
            return x*self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)