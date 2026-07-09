# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # binary tree -> balance 
        # traverse it in O(n)
        node = root
        if node is None:
            return None

        temp = [node.right]
        node.right = self.invertTree(node.left)
        node.left = self.invertTree(temp.pop())
    
        return node

        