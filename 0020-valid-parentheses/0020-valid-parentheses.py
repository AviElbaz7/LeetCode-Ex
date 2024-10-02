class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in matching:
                stack.append(matching[char])
            elif not stack or stack.pop() != char:
                return False
        if stack:
            return False
        return True