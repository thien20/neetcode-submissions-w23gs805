class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) - 2 pointers - sorting
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i and nums[i] == nums[i-1]:
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

                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res

        
        