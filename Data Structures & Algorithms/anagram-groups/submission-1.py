class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            freq = [0]*26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            freq = tuple(freq)
            if freq not in dic:
                dic[freq] = [word]
            
            else:
                dic[freq].append(word)
        
        return list(dic.values())
            