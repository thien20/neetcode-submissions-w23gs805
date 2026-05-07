class Solution:
    def backtrack(self, total, i):
        if total == self.target:
            self.res.append(self.temp[:])
            return

        if i == len(self.nums) or total > self.target:
            return
        self.temp.append(self.nums[i])
        self.backtrack(total + self.nums[i], i)
        self.temp.pop()
        self.backtrack(total, i+1)
        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.target = target
        self.nums = sorted(nums)
        self.total = 0
        self.backtrack(self.total, 0)    
        return self.res