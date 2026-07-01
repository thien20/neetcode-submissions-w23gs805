# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. move pointer to middle to slice it
        # 2. reorder the right-handed linked list
        # 3. merge
        if not head or not head.next:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # we get the slow as the middle cuz 2*slow = fast
        # we should cut it like this
        # ==========================
        middle = slow.next
        slow.next = None
        # ==========================

        prev = None
        while middle:
            nxt = middle.next
            middle.next = prev
            prev = middle
            middle = nxt

        # we already reordered it, just need to take the "prev"
        # we do while loop for reorder cuz len(left) >= len(right)
        reorder = prev
        temp = head
        while reorder:
            nxt = temp.next
            reorder_next = reorder.next

            temp.next = reorder
            reorder.next = nxt

            temp = nxt
            reorder = reorder_next



