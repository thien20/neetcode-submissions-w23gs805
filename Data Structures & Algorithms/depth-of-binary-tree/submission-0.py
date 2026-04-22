# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseTree(self, node: Optional[TreeNode], depth):
        if not node:
            return
        self.res = max(self.res, depth)
        self.traverseTree(node.left, depth + 1)
        self.traverseTree(node.right, depth + 1)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traverseTree(root, 1)
        return self.res