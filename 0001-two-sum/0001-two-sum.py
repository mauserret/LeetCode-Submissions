class Solution(object):
    def twoSum(self, nums, target):
        remain = {}
        for i, num in enumerate(nums):
            if num in remain:
                return [remain[num], i]
            remain[target-num] = i
        
        