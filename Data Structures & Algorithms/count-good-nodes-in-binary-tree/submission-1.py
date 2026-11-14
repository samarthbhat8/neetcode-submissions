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
                node, value = queue.popleft()
                
                if node.val >= value:
                    good += 1

                if node.left:
                    queue.append([node.left, max(node.val, value)])
                if node.right:
                    queue.append([node.right, max(node.val, value)])

        return good
