class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if not char.isnumeric():
                stack.append(char)
            
            if stack and char.isnumeric():
                stack.pop()
        
        return "".join(stack)