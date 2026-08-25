class Solution(object):
    def scoreOfString(self, s):
        tot = 0
        for i in range(1, len(s)):
            tot += abs(ord(s[i-1]) - ord(s[i]))
        return tot
        