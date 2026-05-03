# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseTree(self, node: Optional[TreeNode]):
        if not node:
            return 1
        left = self.traverseTree(node.left)
        right = self.traverseTree(node.right)
        return 1 + max(left, right)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self.traverseTree(root.left)
        right_height = self.traverseTree(root.right)
        return max(left_height, right_height)