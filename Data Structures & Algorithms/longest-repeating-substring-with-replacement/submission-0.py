class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force: for every i we'll check all substring
        # k = # of gaps to fill
        res = 0
        for left in range(len(s)):
            dic = {}
            sub = 0
            for right in range(left, len(s)):
                dic[s[right]] = dic.get(s[right],0) + 1
                sub = max(sub, dic[s[right]])
                if right - left + 1 - sub <= k:
                    res = max(res, right - left + 1)
                    
        return res