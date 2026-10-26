class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        total = [0]
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if grid[r][c] == 0:
                return

            total[0] += grid[r][c]
            grid[r][c] = 0
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    dfs(row, col)
                    if total[0] % k == 0:
                        res += 1
                    total[0] = 0
        return res

        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(row, col):
            visit.add((row, col))
            island_sum = grid[row][col]
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] != 0 and (new_row, new_col) not in visit):
                    island_sum += dfs(new_row, new_col)
            
            return island_sum

            
            
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 0 and (row, col) not in visit:
                    if dfs(row, col) % k == 0:
                        res += 1
        return res
        """
    
        