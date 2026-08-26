class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        dummy_x = x
        rev_x = 0
        while x:
            rev_x = (rev_x * 10) + x % 10
            x //= 10
        return rev_x == dummy_x

        