class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        i0 = nums.index(0)
        
        #check if its cyclically increasing
        is_increasing = True
        for k in range(n):
            if nums[(i0 + k) % n] != k:
                is_increasing = False
                break

        if is_increasing:
            cost1 = i0
            cost2 = 2 + ((n- i0) % n)
            return min(cost1, cost2)
        
        #check if its cyclically decreasing
        is_decreasing = True
        for k in range(n):
            if nums[(i0 - k + n) % n] != k:
                is_decreasing = False
                break

        if is_decreasing:
            cost1 = 1 + (n - 1 - i0)
            cost2 = 1 + ((i0 + 1) % n)
            return min(cost1, cost2)

        return -1
        