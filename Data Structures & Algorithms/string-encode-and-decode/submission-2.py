class Solution:
    # For this constraint, I would propose a method that contain a 
    # encode: list --> number --> delimiter --> that word
    # why this works: able to handle empty string or >20 words
    
    # decode: string --> number(str) --> delimiter --> word
    # method of decode: 2 pointers
    # why delimiter: in coding, separate words and its length, we can start
    # our logic when reaching delimiter
    # if there is no delimiter --> cannot handle word > 10 in length

    # The time complexity would O(n)
    def encode(self, strs: List[str]) -> str:
        msg = ""
        for word in strs:
            msg += str(len(word)) + "#" + word

        return msg

    def decode(self, s: str) -> List[str]:
        # 10#HelloThien5#World
        res = []
        i = 0
        num = ""
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            num = int(s[i:j])
            res.append(s[j+1: j+num+1])
            i = j+num+1
        return res

            







