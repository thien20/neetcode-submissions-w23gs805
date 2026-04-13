class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n^2) - brute force - practice
        # space: O(1)
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]

        return []
        