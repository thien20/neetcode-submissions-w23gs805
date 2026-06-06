class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        dic = {}
        max_freq, left = 0,0
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            # maximum frequency of a ch
            max_freq = max(max_freq, dic[s[right]])

            window_size = right - left + 1
            if window_size - max_freq > k:
                dic[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res