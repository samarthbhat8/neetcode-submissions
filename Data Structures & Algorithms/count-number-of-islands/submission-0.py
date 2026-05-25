class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if r < rows and r >= 0 and c < cols and c >= 0 and grid[r][c] == "1" and (r, c) not in visited:
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands