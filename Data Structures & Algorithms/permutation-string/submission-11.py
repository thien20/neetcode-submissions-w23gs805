class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for i = 1 --> len(s2) - 2
        #   using dictionary --> operation in O(1)
        #   check i:i+2
        window = len(s1)
        target = {}
        for i in range(len(s1)):
            target[s1[i]] = target.get(s1[i],0) + 1
        
        freq = {}
        left = 0
        for right in range(len(s2)):
            freq[s2[right]] = freq.get(s2[right], 0) + 1

            if right - left + 1 > window:
                freq[s2[left]] -= 1
                if freq[s2[left]] == 0:
                    del freq[s2[left]]
                left += 1
            if freq == target:
                return True

        return False