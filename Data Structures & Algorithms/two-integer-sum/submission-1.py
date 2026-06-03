class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in dic:
                return [dic[remainder], i]

            dic[nums[i]] = i