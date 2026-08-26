class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for b in s:
            if b in '({[':
                stack.append(b)
            else:
                if stack and brackets[b] == stack[-1]:
                    stack.pop()
                else:
                    return False         
        return len(stack) == 0