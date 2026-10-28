class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        r, c = len(grid),  len(grid[0])

        # dp[j] = set of XOR values reachable at current row, column j
        dp = [set() for _ in range(c)]
        dp[0].add(grid[0][0])

        for i in range(r):
            for j in range(c):
                # Starting cell
                if i == 0 and j == 0:
                    continue

                current = set()
                # From TOP
                if i > 0:
                    for xor_val in dp[j]:
                        current.add(xor_val ^ grid[i][j])

                # From LEFT
                if j > 0:
                    for xor_val in dp[j - 1]:
                        current.add(xor_val ^ grid[i][j])

                dp[j] = current

        return min(dp[c - 1])