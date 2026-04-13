class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) - 2 pointers - sorting
        nums = sorted(nums)
        res = []
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res
        
        