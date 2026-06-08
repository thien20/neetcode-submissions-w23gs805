class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for i = 1 --> len(s2) - 2
        #   using dictionary --> operation in O(1)
        #   check i:i+2
        window = len(s1)
        freq1 = {}
        for i in range(len(s1)):
            freq1[s1[i]] = freq1.get(s1[i],0) + 1
        
        for i in range(0,len(s2)-window+1):
            freq = {}
            for j in range(i, i+window):
                freq[s2[j]] = freq.get(s2[j], 0) + 1
            print(freq)
            print(freq1)
            if freq == freq1:
                return True

        return False