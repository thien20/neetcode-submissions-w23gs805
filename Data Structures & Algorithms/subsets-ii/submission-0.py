class Solution:
    def backtrack(self, i):
        self.res.append(self.temp[:])

        for index in range(i,len(self.nums)):
            if index > i and self.nums[index] == self.nums[index-1]:
                continue
            self.temp.append(self.nums[index])
            self.backtrack(index+1)
            self.temp.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.nums = sorted(nums)
        self.backtrack(0)
        return self.res