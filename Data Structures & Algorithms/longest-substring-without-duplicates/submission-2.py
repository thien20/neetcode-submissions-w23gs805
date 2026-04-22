class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # "zxyzacb"

        # sliding window
        if not s:
            return 0
        ans = 1
        check_lis = set()
        for left in range(len(s)):
            res = 1
            check_lis.add(s[left])
            for right in range(left+1, len(s)):
                if s[left] == s[right] or s[right] in check_lis:
                    check_lis.clear()
                    break
                res += 1
                check_lis.add(s[right])
                
            ans = max(ans,res)

        return ans