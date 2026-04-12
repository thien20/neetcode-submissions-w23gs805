class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        
        # [-4,-1,-1,0,1,2]
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i+1, len(nums)-1 
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1           
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1

        return res
