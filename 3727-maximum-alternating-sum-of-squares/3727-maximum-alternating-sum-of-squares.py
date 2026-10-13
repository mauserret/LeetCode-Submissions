class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: abs(x))

        l = 0
        r = len(nums) - 1
        tot = 0
        while(l <= r):
            if l == r:
                tot += abs(nums[r]) ** 2
            tot += abs(nums[r]) ** 2
            tot -= abs(nums[l]) ** 2
            r -= 1
            l += 1
        return tot