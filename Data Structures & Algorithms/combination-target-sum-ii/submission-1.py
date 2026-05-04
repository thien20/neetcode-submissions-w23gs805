class Solution:
    def backtrack(self, index, total):
        if total == self.target:
            if self.temp[:] not in self.res:
                self.res.append(self.temp[:])
            return

        if total > self.target or index == len(self.candidates):
            return
        for i in range(index, len(self.candidates)):
            if i > index and self.candidates[i] == self.candidates[i-1]:
                continue
            self.temp.append(self.candidates[i])
            self.backtrack(i+1, total + self.candidates[i])
            self.temp.pop()
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        self.temp = []
        self.target = target
        self.candidates = sorted(candidates)
        self.backtrack(0,0)
        return self.res