class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        count = [0] * 30
        modulo = 10**9 + 7

        for num in nums:
            # because nums[i] < 2^29
            for i in range(30):
                if num & (1 << i):
                    count[i] += 1
        
        res = 0
        for i in range(k):
            curr = 0
            for j in range(29, -1, -1):
                if count[j] > 0:
                    curr |= 1 << j
                    count[j] -= 1
            res = (res + curr * curr) % modulo
        
        return res
        