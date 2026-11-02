class Solution:
    def numberOfSteps(self, num: int) -> int:
        tot = 0
        while num:
            if num & 1: # The number is odd if the bitwise and operator returns 1
                num -= 1
            else:
                num >>= 1
            tot += 1
        return tot