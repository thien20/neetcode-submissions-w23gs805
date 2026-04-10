class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force
        nums = set(nums)
        res = 0
        for num in nums:
            curr, streak = num, 0
            while curr in nums:
                streak += 1
                curr += 1
            res = max(res, streak)                

        return res

            

