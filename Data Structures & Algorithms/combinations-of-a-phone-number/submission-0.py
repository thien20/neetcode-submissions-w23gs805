class Solution:
    def backtrack(self, i):
        if i == len(self.digits):
            self.res.append("".join(self.temp))
            return

        digit = self.digits[i]
        for ch in self.dic[digit]:
            self.temp.append(ch)
            self.backtrack(i+1)
            self.temp.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.res = []
        self.temp = []
        self.digits = digits
        self.sub = ""
        self.backtrack(0)
        return self.res