# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head
        
        curr = head
        prev, n = None, head.next 
        
        while curr:
            n = curr.next
            curr.next = prev

            prev = curr
            curr = n
        
        return prev