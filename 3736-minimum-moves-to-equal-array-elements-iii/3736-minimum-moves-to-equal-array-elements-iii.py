class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        tot = 0
        for num in nums:
            tot += max_num - num
        return tot
        