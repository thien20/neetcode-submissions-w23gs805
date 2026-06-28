# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # because fast is the one can be crashed if there’s no cycle otherwise fast meets slow
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
