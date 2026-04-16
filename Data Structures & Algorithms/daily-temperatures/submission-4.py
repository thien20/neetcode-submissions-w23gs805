class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack

        stack = []
        res = [0] * len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                tm_i, tm_t = stack.pop()
                res[tm_i] = ind - tm_i
            stack.append((ind,temp))

        return res
