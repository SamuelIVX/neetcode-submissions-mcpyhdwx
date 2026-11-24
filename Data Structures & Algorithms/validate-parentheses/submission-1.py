class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {"(":")","{":"}", "[":"]"}

        for char in s:
            if char in parenthesis:
                stack.append(char)
            elif stack and parenthesis[stack[-1]] == char:
                stack.pop()
            else:
                return False

        return True if not stack else False
            