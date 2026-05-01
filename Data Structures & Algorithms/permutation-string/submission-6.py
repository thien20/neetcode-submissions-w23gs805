class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        target = [0] * 26
        for cha in s1:
            target[ord(cha) - ord('a')] += 1

        window = [0] * 26
        left = 0
        for i in range(len(s2)):
            window[ord(s2[i]) - ord('a')] += 1

            if i - left + 1 > len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if window == target:
                print(window, s1)
                return True

    
        return False