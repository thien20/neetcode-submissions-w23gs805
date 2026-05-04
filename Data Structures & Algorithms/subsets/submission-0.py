class Solution:
    def backtrack(self, i):
        if i == len(self.nums):
            self.res.append(self.temp[:])
            return
        self.temp.append(self.nums[i])
        self.backtrack(i+1)
        self.temp.pop()
        self.backtrack(i+1)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.nums = nums
        self.backtrack(0)
        return self.res
