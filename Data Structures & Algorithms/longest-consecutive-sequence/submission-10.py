class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        for num in nums:
            length = 1
            while num + length in nums:
                length += 1

            ans = max(ans, length)

        return ans
