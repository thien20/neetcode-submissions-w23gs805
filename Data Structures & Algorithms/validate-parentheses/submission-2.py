class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = {"{":1,"(":2,"[":3}
        close_brackets = {1:"}",2:")",3:"]"}
        left = 0
        while left < len(s):
            if len(stack) == 0 or open_brackets.get(s[left]):
                stack.append(s[left])
                left += 1
                continue

            elif stack:
                open_sign = open_brackets.get(stack.pop())
                if close_brackets.get(open_sign) == s[left]:
                    left += 1
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False