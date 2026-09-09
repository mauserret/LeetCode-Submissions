class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        barrier = 1000
        while n >= barrier:
            count += (n - barrier + 1)
            barrier *= 1000
        return count

        