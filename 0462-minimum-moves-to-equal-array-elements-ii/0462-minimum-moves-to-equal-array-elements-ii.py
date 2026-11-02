class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        tot = 0
        mid = nums[n//2]
        
        for num in nums:
            tot += abs(num - mid)
        return tot
