class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        tot = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                tot += len(seen) ** 2
        return tot
        