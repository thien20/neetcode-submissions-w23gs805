# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, lower, upper):
            if node is None:
                return True

            if lower >= node.val or upper <= node.val:
                return False

            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root, float("-inf"), float("inf"))