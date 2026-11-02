class Solution:
    def numberOfSteps(self, num: int) -> int:
        tot = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
            tot += 1
        return tot