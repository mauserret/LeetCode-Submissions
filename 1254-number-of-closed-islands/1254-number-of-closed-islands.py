class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False
            if grid[row][col] == 1 or (row, col) in seen:
                return True
            if row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1:
                return False

            seen.add((row, col))
            one = dfs(row - 1, col) 
            two = dfs(row + 1, col) 
            three = dfs(row, col - 1) 
            four = dfs(row, col + 1)
            return one and two and three and four


        res = 0
        for row in range(1,ROWS-1):
            for col in range(1,COLS-1):
                if grid[row][col] == 0 and (row, col) not in seen:
                    if dfs(row, col): 
                        res += 1
        return res
           