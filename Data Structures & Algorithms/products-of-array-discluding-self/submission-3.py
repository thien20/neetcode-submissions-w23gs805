class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        res = [0] * len(nums)
        for i in range(len(nums)):
            final_prod = 1
            for j in range(len(nums)): 
                if i != j:   
                    final_prod *= nums[j]

            res[i] = final_prod
        return res


