class Solution:
    def maxDistinct(self, s: str) -> int:
        chars = []
        for c in s:
            if c not in chars:
                chars.append(c)
        return len(chars)