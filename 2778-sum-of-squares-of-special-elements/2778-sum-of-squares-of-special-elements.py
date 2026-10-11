class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        tot = 0
        for i in range(1,n+1):
            print(n % i)
            if n % i == 0:
                tot = tot + (nums[i-1] * nums[i-1])
        return tot