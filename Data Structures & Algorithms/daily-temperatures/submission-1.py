class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = [30,38,30,36,35,40,28]
        
        # Return an array result where result[i] is the number of days
        # after the ith day before a warmer temperature appears
        # result = [1,4,1,2,1,0,0]
        res = [0] * len(temperatures)
        # left, right = 0, 1
        # while right < len(temperatures):
        #     if temperatures[right] > temperatures[left]:
        #         print(temperatures[left], temperatures[right])
        #         res[left] = right-left
        #         left += 1
        #         right = left + 1
        #     else:
        #         right += 1

        for left in range(len(temperatures)):
            for right in range(left+1,len(temperatures)):
                if temperatures[right] > temperatures[left]:
                    res[left] = right-left
                    break
        # 30,29,28,36,32,43,78
        #
        return res
        
