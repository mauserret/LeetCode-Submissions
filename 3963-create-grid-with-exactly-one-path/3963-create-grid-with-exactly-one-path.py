class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Basically just do another path different from leetcode's
        # Whole horizontal line with dots for the first array, then g
        grid = []
        grid.append("." * n)
        for i in range(m - 1):
            grid.append("#" * (n - 1) + ".") 
        return grid
        