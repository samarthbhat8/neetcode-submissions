# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        good = 0
        queue = deque()
        queue.append([root, root.val])

        while queue:
            for i in range(len(queue)):
                retard, value = queue.popleft()
                
                if retard.val >= value:
                    good += 1

                if retard.left:
                    queue.append([retard.left, max(retard.val, value)])
                if retard.right:
                    queue.append([retard.right, max(retard.val, value)])

        return good
