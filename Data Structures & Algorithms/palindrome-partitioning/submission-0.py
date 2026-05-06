class Solution:
    def isPalin(self, substr):
        if len(substr) == 0:
            return False
        left, right = 0, len(substr)-1
        while left < right:
            if substr[left] != substr[right]:
                return False
            left += 1
            right -= 1
        return True
    def backtrack(self, i):
        if i == len(self.s):
            self.res.append(self.temp[:])
            return
        
        for right in range(i+1, len(self.s)+1):
            substr = self.s[i:right]

            if self.isPalin(substr):
                self.temp.append(substr)        
                self.backtrack(right)
                self.temp.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.s = s
        self.sub = ""
        self.backtrack(0)
        return self.res