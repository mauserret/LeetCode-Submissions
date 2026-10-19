class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i, n in enumerate(sorted(nums)):
            if n == target:
                res.append(i)
        return res
        