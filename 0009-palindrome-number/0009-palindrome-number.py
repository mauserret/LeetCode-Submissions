class Solution(object):
    def isPalindrome(self, x):
        """
        if x < 0:
            return False
        dummy_x = x
        new_x = 0
        while x:
            new_x = (new_x * 10) + x % 10
            x //= 10
        return new_x == dummy_x
        """
        if x < 0:
            return False
        return x == int(str(x)[::-1])

        