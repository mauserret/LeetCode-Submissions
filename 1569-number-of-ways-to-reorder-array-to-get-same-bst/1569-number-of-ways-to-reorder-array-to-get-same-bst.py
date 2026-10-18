class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        modulo, n = 10**9 + 7, len(nums)
        born = [-1] * (n + 2) # walls at 0 and n + 1 (insertion time of each val)
        for i, x in enumerate(nums):
            born[x] = i
        
        sizes, stack = 1, [0]
        for v in range(1, n + 2):
            while born[stack[-1]] > born[v]: # here v is the right wall of the value on top
                stack.pop()
                sizes = sizes * (v - stack[-1] - 1 ) % modulo # therefore the value below it is the left wall
            stack.append(v)
        
        fact = 1
        for k in range(2, n + 1):
            fact = fact * k % modulo
        return (fact * pow(sizes, -1, modulo) - 1) % modulo