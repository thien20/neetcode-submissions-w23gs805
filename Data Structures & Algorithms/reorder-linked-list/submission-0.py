# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        # split linkedlist into 2 halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        

        second = prev
        # merge
        while second:
            temp1 = head.next
            temp2 = second.next

            head.next = second
            second.next = temp1

            head = temp1
            second = temp2



        