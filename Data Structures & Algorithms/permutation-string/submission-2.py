class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        target = [0] * 26
        window = [0] * 26

        for ch in s1:
            target[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(n):
            # Add right character into window
            window[ord(s2[right]) - ord('a')] += 1

            # If window size is larger than len(s1), shrink from left
            if right - left + 1 > m:
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # If same frequency, current window is a permutation
            if window == target:
                return True

        return False