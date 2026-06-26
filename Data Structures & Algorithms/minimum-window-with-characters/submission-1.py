class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        left = 0
        countT, window = {}, {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        have, need = 0, len(countT)
        res, currentLen = [-1,-1], float("inf")
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need: # valid
                if (right - left + 1) < currentLen: # found minimum
                    currentLen = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1

        left, right = res
        return s[left:right + 1] if currentLen else ""

