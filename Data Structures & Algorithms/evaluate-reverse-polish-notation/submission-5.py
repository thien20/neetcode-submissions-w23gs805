class Solution:
    def recursion(self, tokens):
        token = tokens.pop()
        if token not in "+-*/":
            return int(token)

        left = self.recursion(tokens)
        right = self.recursion(tokens)

        if token == "+":
            return left + right
        if token == "-":
            return right - left
        if token == "*":
            return left * right
        if token == "/":
            return int(right / left)
    def evalRPN(self, tokens: List[str]) -> int:
        # recursion
        return self.recursion(tokens)
        

