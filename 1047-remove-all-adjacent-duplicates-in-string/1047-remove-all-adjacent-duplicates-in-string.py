class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char != stack[-1]:
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
        