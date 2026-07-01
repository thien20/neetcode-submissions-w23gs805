# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # we can guarantee that slow can never reach the None before fast
        # so we do need to check slow.next
        # 1 more thing is fast is gonna be move faster in progress
        # so we want to check whether it is None or not
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
