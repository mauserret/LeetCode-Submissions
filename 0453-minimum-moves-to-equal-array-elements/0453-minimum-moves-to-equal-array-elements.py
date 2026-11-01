class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """
        min_num = min(nums)
        tot = 0
        for num in nums:
            tot += abs(num - min_num)
        return tot
        """
        return sum(nums) - min(nums) * len(nums)
        
        