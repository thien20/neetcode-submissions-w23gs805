class Solution:
    def binary_s_halves(self, left, right):
        while left <= right:
            mid = (left + right) // 2

            if self.nums[mid] == self.target:
                return mid
            elif self.nums[mid] < self.target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        pivot = left

        res = self.binary_s_halves(0, pivot - 1)
        if res != -1:
            return res
        return self.binary_s_halves(pivot, len(nums)-1)