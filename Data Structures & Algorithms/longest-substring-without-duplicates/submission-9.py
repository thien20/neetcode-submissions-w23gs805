class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in dic:
                # we shrink window / update left / shift left + 1
                left = max(left, dic.get(s[right]) + 1)
            dic[s[right]] = right # store the index of that char
            ans = max(ans, right - left + 1)

        return ans
                