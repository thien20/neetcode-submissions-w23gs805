class Solution:
    def doPermute(self, i):
        if i == len(self.nums):
            if self.nums[:] in self.res:
                return
            self.res.append(self.nums[:])
            return
        for j in range(len(self.nums)):
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.doPermute(i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.doPermute(0)
        return self.res