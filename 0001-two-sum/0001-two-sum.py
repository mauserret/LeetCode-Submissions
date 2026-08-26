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
        """
        loop i through nums
            loop j through from i to the end of nums
                if nums[i] + nums [j] is target 
                then return [i,j]
        """
        table = {}
        for i in range(len(nums)):
            
            if nums[i] in table:
                return [table[nums[i]], i]
            remain = target - nums[i]
            table[remain] = i

        