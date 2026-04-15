class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for left in range(len(temperatures)):
            right = left + 1
            while right < len(temperatures):
                if temperatures[right] > temperatures[left]:
                    res[left] = right-left
                    break
                right += 1
        return res
        
