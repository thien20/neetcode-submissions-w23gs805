class Solution:
    def trap(self, height: List[int]) -> int:
        # time: O(n) - stack
        # space: O(n) - stack
        if not height:
            return 0

        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid_block = height[stack.pop()]
                if stack:
                    right_wall = height[i]
                    left_wall = height[stack[-1]]
                    h = min(right_wall,left_wall) - mid_block
                    w = i - stack[-1] -1
                    res += h*w

            stack.append(i)

        return res