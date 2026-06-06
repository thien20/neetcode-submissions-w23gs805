class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for left in range(len(s)):
            # for each "ch" we check all the substring --> O(n^2)
            dic = {}
            sub = 0
            for right in range(left,len(s)):
                dic[s[right]] = dic.get(s[right], 0) + 1
                sub = max(sub, dic[s[right]])
                if right - left + 1 - sub <= k:
                    res = max(res, right-left+1)
        
        return res