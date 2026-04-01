import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num,0) + 1

        dic = list(sorted(dic, key=dic.get, reverse=True))[:k]


        return dic