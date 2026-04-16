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
        node = root
        temp = []
        if node == None:
            return
        temp.append(node.right)
        node.right = self.invertTree(node.left)
        node.left = self.invertTree(temp.pop())
        

        return node


