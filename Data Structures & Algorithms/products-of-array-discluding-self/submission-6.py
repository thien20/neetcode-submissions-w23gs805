class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and post
        # [1,2,4,6] --> num
        # [1,1,2,8] --> res / pre
        # 24
        # [,12,8]

        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        


