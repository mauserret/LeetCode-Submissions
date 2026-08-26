class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for b in s:
            if b in brackets.keys():
                if stack and brackets[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if stack:
            return False
        return True  