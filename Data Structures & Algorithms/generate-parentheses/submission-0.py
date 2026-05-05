class Solution:
    def backtrack(self, temp, left, right):
        if left == right == self.n:
            self.res.append(temp)
            return
        if left < self.n:
            self.backtrack(temp + "(", left + 1, right)
        if right < left:
            self.backtrack(temp + ")", left, right + 1)
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        temp = ""
        self.n = n
        self.backtrack(temp, 0, 0)
        return self.res