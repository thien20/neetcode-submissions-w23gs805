# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def help(node):
            if node is None:
                return 0

            left = help(node.left)
            right = help(node.right)

            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        help(root)
        return self.ans
            