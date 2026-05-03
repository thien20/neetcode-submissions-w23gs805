# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkHeight(self, node):
        if node is None:
            return 0
        left = self.checkHeight(node.left)
        right = self.checkHeight(node.right)
        return 1 + max(left, right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        height_left = self.checkHeight(root.left)
        height_right = self.checkHeight(root.right)
        if abs(height_left - height_right) > 1:
            return False
        # We need to need handle balance for every subtree
        return self.isBalanced(root.left) and self.isBalanced(root.right)