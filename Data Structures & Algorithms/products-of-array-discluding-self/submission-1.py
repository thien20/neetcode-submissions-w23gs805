class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        zero_indices = []
        isZero = False
        for i in range(len(nums)):
            if nums[i] != 0:
                temp *= nums[i]
            else:
                isZero = True
                zero_indices.append(i)

        if len(zero_indices) > 1: return [0]* len(nums)

        res = [0] * len(nums)
        for i in range(len(nums)):
            if isZero:
                if i not in zero_indices:
                    res[i] = 0
                    continue
                else:
                    res[i] = temp if nums[i] == 0 else temp
                    continue
            else:
                res[i] = int(temp/nums[i])

        
        return res


