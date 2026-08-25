class Solution(object):
    def buildArray(self, nums):
        return [nums[num] for num in nums] 
        """
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans
        """