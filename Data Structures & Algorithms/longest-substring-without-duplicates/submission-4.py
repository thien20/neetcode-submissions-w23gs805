class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # "zxyzacb"

        # sliding window
        if not s:
            return 0
        res = 0
        dic = {}
        left = 0
        for right in range(len(s)):
            if s[right] in dic:
                left = max(left, dic.get(s[right])+1)
                
            dic[s[right]] = right
            res = max(res, right - left + 1)
        
        return res