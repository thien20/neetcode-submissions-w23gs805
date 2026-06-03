class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums)+1)]
        for number, freq in dic.items():
            bucket[freq].append(number)

        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans

        return ans 