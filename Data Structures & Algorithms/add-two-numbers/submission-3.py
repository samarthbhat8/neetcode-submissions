# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(None)
        
        carry = 0
        
        while l1 and l2:
            s = l1.val + l2.val + carry
            if s > 9:
                carry = 1
            else:
                carry = 0
            s = s % 10
            curr.next = ListNode(s, None)

            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + carry
            if s > 9:
                carry = 1
            else:
                carry = 0
            s = s % 10
            curr.next = ListNode(s, None)
            curr = curr.next
            l1 = l1.next

        while l2:
            s = l2.val + carry
            if s > 9:
                carry = 1
            else:
                carry = 0
            s = s % 10
            curr.next = ListNode(s, None)
            curr = curr.next
            l2 = l2.next


        
        if carry == 1:
            curr.next = ListNode(1, None)

        return dummy.next


