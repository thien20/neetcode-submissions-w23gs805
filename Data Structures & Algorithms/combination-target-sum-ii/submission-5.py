class Solution:
    def backtrack(self, total, i):
        if total == self.target:
            if self.temp[:] in self.res:
                return
            self.res.append(self.temp[:])
            return

        if i > len(self.candidates) or total > self.target:
            return

        for right in range(i, len(self.candidates)):
            if right > i and self.candidates[right] == self.candidates[right-1]:
                continue
            self.temp.append(self.candidates[right])
            self.backtrack(total + self.candidates[right], right+1)
            self.temp.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.candidates = sorted(candidates)
        self.target = target
        self.total = 0
        self.backtrack(self.total, 0)
        return self.res
        