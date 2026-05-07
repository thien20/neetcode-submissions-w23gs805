class Solution:
    def backtrack(self, i):
        if i == len(self.nums):
            self.res.append(self.nums[:])
            return

        for j in range(i, len(self.nums)):
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.backtrack(i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.backtrack(0)
        return self.res    