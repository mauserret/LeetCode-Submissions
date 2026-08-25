class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = 0
        num2 = 0
        for i in range(1, n+1):
            if i % m:
                num1 += i
            else:
                num2 += i
        print(num1)
        print(num2)
        return num1 - num2
