# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedlist(self, head):
        prev = None
        curr = head
        while curr:
            nxt_curr = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_curr

        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            num = v1 + v2 + carry
            
            carry = num // 10
            digit = num % 10

            tail.next = ListNode(digit)
            tail = tail.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
        
        return dummy.next






