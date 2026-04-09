class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]
        # [48,24,12,8]
        res = [0] * len(nums)
        pref = [0] * len(nums)
        suff = [0] * len(nums)

        pref[0] = suff[len(nums)-1] = 1

        for i in range(1,len(nums)):
            pref[i] = nums[i-1] * pref[i-1]
        print(pref)
        for i in range(len(nums)-2,-1,-1):
            suff[i] = nums[i+1] * suff[i+1]
        print(suff)
        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]

        return res

