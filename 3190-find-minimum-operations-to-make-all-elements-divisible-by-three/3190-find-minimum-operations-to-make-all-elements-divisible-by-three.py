class Solution(object):
    def minimumOperations(self, nums):
        tot = 0
        for num in nums:
            tot += min(num % 3, 3 - num % 3)
        return tot