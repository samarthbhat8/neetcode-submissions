# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathsum = float("-inf")

        self.dfs(root)

        return self.pathsum

    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.pathsum = max(self.pathsum, root.val + left + right, root.val, root.val + left, root.val + right)

        return root.val + max(left, right, 0)
