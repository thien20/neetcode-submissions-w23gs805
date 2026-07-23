# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        curr = deque([root])

        while curr:
            res_level = []
            for i in range(len(curr)):
                node = curr.popleft()
                if node:
                    res_level.append(node.val)
                    curr.append(node.left)
                    curr.append(node.right)

            if res_level:
                res.append(res_level)

        return res