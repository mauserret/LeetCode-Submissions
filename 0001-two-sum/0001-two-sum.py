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
        dic = {} # 7:0 
        for i in range(len(nums)): #nums = [2, 7, 11, 9] targert = 9
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[target - nums[i]] = i
                