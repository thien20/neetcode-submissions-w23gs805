class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = [0] * 26
        dic_t = [0] * 26

        for ch in s:
            dic_s[ord(ch) - ord('a')] += 1
        
        for ch in t:
            dic_t[ord(ch) - ord('a')] += 1

        return True if dic_s == dic_t else False