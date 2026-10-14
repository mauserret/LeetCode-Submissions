class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        """
        if sum > 9 * num:
            return ""
        res = []
        for _ in range(num):
            d = min(9, sum)
            res.append(str(d))
            sum -= d
        return "".join(res)
        """
        if sum > 9 * num:
            return ""

        full_nines = sum // 9
        remainder = sum % 9

        # Case 1: sum is an exact multiple of 9
        if remainder == 0:
            return "9" * full_nines + "0" * (num - full_nines)

        # Case 2: remainder digit present between 9s and 0s
        zeros = num - full_nines - 1
        return "9" * full_nines + str(remainder) + "0" * zeros
       
        