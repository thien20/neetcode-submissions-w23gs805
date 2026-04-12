class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0: # 1+2+3>0 and this array is sorted
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left],nums[right], nums[i]])
                    left += 1
                    right -= 1
                    # deduplicate:
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1

        return res
