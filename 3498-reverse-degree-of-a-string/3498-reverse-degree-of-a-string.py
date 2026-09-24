class Solution:
    def reverseDegree(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            tot += (27 - (ord(s[i]) - 96)) * (i+1)
        return tot