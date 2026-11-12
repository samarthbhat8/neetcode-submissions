# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First find the middle of the list
        # Reverse the second half
        # Merge both lists in order

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse = slow.next
        slow.next = None
        prev = None


        while reverse:
            nxt = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = nxt
        
        list1, list2 = head, prev

        while list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2     