# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Imitate the first principle thinking of the way we do multiplication in school.
# Take care of python functions and their expectations of input format, reverse the strings as we start from the end.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n = len(num1)
        m = len(num2)
        if n<m:
            return self.multiply(num2, num1)
        
        res=""; zero = 0
        for i in range(m-1, -1, -1):
            curr = self.mul(num1, num2[i], zero)
            res = self.add(res, curr)
            zero+=1
        return res

    def mul(self, num, digit, zero):
        res=[]#can't be string, no append function
        if digit == "0":
            return res
        digit = int(digit)
        carry = 0; n = len(num)-1
        while n>=0 or carry:
            m = int(num[n]) if n>=0 else 0
            prod = digit*m+carry
            res.append(str(prod%10)) #Imp: can't be res.append(prod%10), fix in return TypeError as join expects only string
            carry=prod//10
            n-=1
        return ''.join(res[::-1]) + '0'*zero
    
    def add(self, num1, num2):
        n = len(num1)-1
        m = len(num2)-1
        res=[]; carry = 0
        while n>=0 or m>=0 or carry:
            n1 = int(num1[n]) if n>=0 else 0
            n2 = int(num2[m]) if m>=0 else 0
            curr = n1 + n2 + carry
            carry = curr//10
            res.append(str(curr%10))
            n-=1
            m-=1
        return ''.join(res[::-1])
        