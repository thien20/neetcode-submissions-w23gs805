class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        res = 0
        for i in range(len(nums)):
            length = 1
            curr = nums[i]
            while dic.get(curr+1):
                length += 1
                curr += 1

            res = max(length, res)
        return res
    
            

