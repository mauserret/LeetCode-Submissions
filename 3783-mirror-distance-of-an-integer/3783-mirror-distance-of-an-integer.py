class Solution(object):
    def mirrorDistance(self, n):
        def reverse(n):
            new_n = 0
            while n:
                digit = n % 10
                new_n = (new_n * 10) + digit
                n //= 10
            return new_n
        return abs(n-reverse(n))


        