class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        # [10,13,11,12,11]
        # {10: 1,
        #  11: 2
        #  12: 1
        #  13: 1}

        # 
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        
        res = 0
        for num in nums:
            if dic.get(num):
                length = 1
                while dic.get(num+length):
                    length += 1
                res = max(res, length)

        return res

            

