# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if node is None:
            # True for balance because for the case empty tree
            # it should be true
            # [balanced, height]
            return [True, 0]
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balance, 1 + max(left[1], right[1])]
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs
        return self.dfs(root)[0]
