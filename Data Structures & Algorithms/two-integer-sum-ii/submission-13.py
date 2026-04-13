class Solution:
    def bs(self, numbers, target, index_i):
        left, right = index_i, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(nlogn) - binary search - sorted array - practice
        # space: O(1)
        for i in range(len(numbers)):
            num_to_find = target - numbers[i]
            j = self.bs(numbers, num_to_find, i+1)
            if j != -1:
                return [i+1, j+1]
        return []
        