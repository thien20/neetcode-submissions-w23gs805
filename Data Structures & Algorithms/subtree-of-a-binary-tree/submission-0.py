# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return False

        if self.isSame(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        
        return False

        