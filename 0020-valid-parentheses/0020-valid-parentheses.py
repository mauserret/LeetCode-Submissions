class Solution(object):
    def isValid(self, s):
        """
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
                if not stack or brackets[b] != stack[-1]:
                    return False
                stack.pop()
                    
        return len(stack) == 0
        """
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""