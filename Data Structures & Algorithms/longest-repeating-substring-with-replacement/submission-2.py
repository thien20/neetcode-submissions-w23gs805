class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # shrinking window
        left, sub, res = 0, 0, 0
        dic = {}
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            sub = max(sub, dic[s[right]])
            while right - left + 1 - sub > k:
                dic[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res