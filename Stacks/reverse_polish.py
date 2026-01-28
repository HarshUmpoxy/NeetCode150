class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                # token is a number
                stack.append(int(token))
            else:
                # token is an operator
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # "/"
                    stack.append(int(a / b))  # truncate toward zero

        return stack[-1]
