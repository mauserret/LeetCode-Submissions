class Solution:
    def reverseDegree(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            tot += (123 - ord(s[i])) * (i+1)
        return tot