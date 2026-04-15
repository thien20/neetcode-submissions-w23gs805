class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        # [30,38,30,36,35,40,28]
        # 
        # []
        # res = [1,4,1,2,1,0,0]
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                print(stack)
                tm_i, tm_t = stack.pop()
                res[tm_i] = index - tm_i
            stack.append((index,temp))


        return res
        
