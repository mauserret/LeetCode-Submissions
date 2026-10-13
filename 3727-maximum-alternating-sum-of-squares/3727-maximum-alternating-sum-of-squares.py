class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
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
        """
        numsSquared = [n * n for n in nums]
        numsSquared.sort()
        # basically we want to sum the numbers that are biggest so from half to end and substract the smallest from start to half - 1
        pos = len(nums) // 2
        return sum(numsSquared[pos:]) - sum(numsSquared[:pos]) 