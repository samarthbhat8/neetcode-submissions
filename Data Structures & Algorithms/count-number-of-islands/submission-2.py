class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, columns = len(grid), len(grid[0])
        islands = 0


        def bfs(row, column):
            visited.add((row, column))
            queue = deque()
            queue.append((row, column))

            while queue:
                r, c = queue.popleft()
                if r + 1 >= 0 and r + 1 < rows and c >= 0 and c < columns and (r + 1, c) not in visited and grid[r + 1][c] == "1":
                    visited.add((r + 1, c))
                    queue.append((r + 1, c))
                if r - 1 >= 0 and r - 1 < rows and c >= 0 and c < columns and (r - 1, c) not in visited and grid[r - 1][c] == "1":
                    visited.add((r - 1, c))
                    queue.append((r - 1, c))
                if r >= 0 and r < rows and c + 1 >= 0 and c + 1 < columns and (r, c + 1) not in visited and grid[r][c + 1] == "1":
                    visited.add((r, c + 1))
                    queue.append((r, c + 1))
                if r >= 0 and r < rows and c - 1 >= 0 and c - 1 < columns and (r, c - 1) not in visited and grid[r][c - 1] == "1":
                    visited.add((r, c - 1))
                    queue.append((r, c - 1))

        for r in range(rows):
            for c in range(columns):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands

