class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n^2) - brute force
        # space: O(1)
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1, i, -1):
                edge_min = min(heights[i], heights[j])
                res = max(res, edge_min*(j-i))

        return res