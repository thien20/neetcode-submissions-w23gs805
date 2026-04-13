class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n) - 2 pointers
        # space: O(1)
        res = 0
        left, right = 0, len(heights) - 1
        while left < right:
            min_edge = min(heights[left], heights[right])
            res = max(res, min_edge*(right-left))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            
            

        return res