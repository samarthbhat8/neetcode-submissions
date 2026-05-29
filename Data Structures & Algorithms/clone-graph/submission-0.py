"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = set()
        originalToClone = {}
        
        def dfs(node):
            if node in visited:
                return originalToClone[node]
            
            visited.add(node)
            originalToClone[node] = Node(node.val)
            
            for n in node.neighbors:
                originalToClone[node].neighbors.append(dfs(n))

            return originalToClone[node]

        return dfs(node)
