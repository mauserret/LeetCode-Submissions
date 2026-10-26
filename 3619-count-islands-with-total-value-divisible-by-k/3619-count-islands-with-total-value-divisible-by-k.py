class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        tot = [0]
        def dfs(row, col):
            if ((row, col) in visit or row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == 0):
                return 0
            
            visit.add((row, col))
            return (grid[row][col] + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))

            
            
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 0 and (row, col) not in visit:
                    if dfs(row, col) % k == 0:
                        res += 1
        return res
    
        