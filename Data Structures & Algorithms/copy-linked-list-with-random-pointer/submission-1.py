"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. Iterate through original list, create copy of each node, link to next node
        # 2. Iterate through original list again, link randoms of the copy

        curr = head

        hashmap = {None : None} # original : copy

        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]