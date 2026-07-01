"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a dic stores independent node,
        # those node still has their original connection
        # retrieve those connection and assign to the copy/nodes dic
        # return that dic
        if not head:
            return None
        dic = {}
        curr = head
        # dic = { NodeA: Node(NodeA.val) }
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = dic[curr]
            copy.next = dic.get(curr.next)
            copy.random = dic.get(curr.random)
            curr = curr.next

        return dic[head]
