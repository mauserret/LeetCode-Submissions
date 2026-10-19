class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        res = []
        for i, n in enumerate(sorted(nums)):
            if n == target:
                res.append(i)
        return res
        """
        if target not in nums:
            return []
        nums.sort()
        res = []
        for i in range(nums.index(target), len(nums)):
            if nums[i] != target:
                break
            res.append(i)
        return res


        