class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # "zxyzacb"

        # sliding window
        if not s:
            return 0
        ans = 0
        check_lis = set()
        left = 0
        for right in range(len(s)):
            while s[right] in check_lis:
                check_lis.remove(s[left])
                left += 1
            check_lis.add(s[right])
            ans = max(ans, right - left + 1)

        return ans