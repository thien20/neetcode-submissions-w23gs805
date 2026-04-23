# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trackHeight(self, node):
        if node is None:
            return 0

        
        left = self.trackHeight(node.left)
        right = self.trackHeight(node.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs
        self.res = 0
        self.trackHeight(root)
        return self.res

