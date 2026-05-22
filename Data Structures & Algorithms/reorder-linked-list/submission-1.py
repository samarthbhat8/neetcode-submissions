# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse = slow.next
        slow.next = None
        prev = None

        while reverse:
            n = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = n

        first, second = head, prev
        
        while second:
            f = first.next
            s = second.next
            first.next = second
            second.next = f
            first = f
            second = s

