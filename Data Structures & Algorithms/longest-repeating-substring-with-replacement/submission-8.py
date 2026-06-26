class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, ans = 0,0
        seen = {}
        max_freq_ch = 0
        for right, ch in enumerate(s):
            seen[ch] = seen.get(ch, 0) + 1
            max_freq_ch = max(max_freq_ch, seen[ch])
            window = right - left + 1
            if window - max_freq_ch > k: # invalid
                # shrinking + update left
                seen[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans