class Solution:
    def getMaxRate(self, piles):
        max_rate = 0
        for banana in piles:
            if banana > max_rate:
                max_rate = banana
        return max_rate
    def isRateValid(self, piles, rate, h):
        total = 0
        for banana in piles:
            total += math.ceil(banana/rate)
        return total <= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = self.getMaxRate(piles)
        res = max_rate
        left, right = 1, max_rate
        while left <= right:
            rate = (left + right) // 2
            if self.isRateValid(piles, rate, h):
                res = min(rate, res)
                right = rate - 1
            else:
                left = rate + 1

        return res
