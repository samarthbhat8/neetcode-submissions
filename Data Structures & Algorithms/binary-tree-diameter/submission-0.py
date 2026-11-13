# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        self.height(root)
        return self.result

    def height(self, root):
        if not root:
            return 0

        self.result = max(self.result, self.height(root.left) + self.height(root.right))
        return 1 + max(self.height(root.left), self.height(root.right))
