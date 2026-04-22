# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # binray tree -> balance 
        # traverse it in O(n)
        stack = []
        if root is None:
            return
        stack.append(root.right)
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(stack.pop())

        return root