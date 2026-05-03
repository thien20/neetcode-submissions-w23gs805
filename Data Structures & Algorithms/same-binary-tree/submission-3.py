# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq1 = deque([p])
        dq2 = deque([q])

        while dq1 and dq2:
            for _ in range(len(dq1)):
                nodeP = dq1.popleft()
                nodeQ = dq2.popleft()

                if nodeP is None and nodeQ is None:
                    continue

                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                dq1.append(nodeP.left)
                dq1.append(nodeP.right)
                dq2.append(nodeQ.left)
                dq2.append(nodeQ.right)

        return True