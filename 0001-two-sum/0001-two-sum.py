class Solution(object):
    def twoSum(self, nums, target):
        """
        remain = {}
        for i, num in enumerate(nums):
            if num in remain:
                return [remain[num], i]
            remain[target-num] = i
        """
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                