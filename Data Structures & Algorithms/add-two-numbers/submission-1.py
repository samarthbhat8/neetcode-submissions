# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            sum = val1 + val2 + carry

            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0

            curr.next = ListNode(sum)

            if l1:
                l1 = l1.next
            else:
                l1 = 0
            
            if l2:
                l2 = l2.next
            else:
                l2 = 0
            
            curr = curr.next
        
        return dummy.next
        
