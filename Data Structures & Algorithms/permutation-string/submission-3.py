class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        target = {}
        for ch in s1:
            target[ch] = target.get(ch, 0) + 1

        left = 0
        window = {}

        for right in range(len(s2)):
            # Add right char
            ch = s2[right]
            window[ch] = window.get(ch, 0) + 1

            # Keep window size fixed as len(s1)
            if right - left + 1 > len(s1):
                left_ch = s2[left]
                window[left_ch] -= 1

                if window[left_ch] == 0:
                    del window[left_ch]

                left += 1

            # Check exact frequency match
            if window == target:
                return True

        return False