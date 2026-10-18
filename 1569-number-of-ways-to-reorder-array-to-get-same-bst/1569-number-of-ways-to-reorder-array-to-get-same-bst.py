class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        n = len(nums)
        born = [-1] * (n + 2) # walls at 0 and n + 1 (insertion time of each val)
        for i, x in enumerate(nums):
            born[x] = i
        
        sizes, stack = 1, [0]
        for v in range(1, n + 2):
            while born[stack[-1]] > born[v]: # here v is the right wall of the value on top
                stack.pop()
                sizes *= v - stack[-1] - 1 # therefore the value below it is the left wall
            stack.append(v)
        
        return (factorial(n) // sizes - 1) % (10**9 + 7)