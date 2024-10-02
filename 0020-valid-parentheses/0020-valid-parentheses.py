class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in matching:
                stack.append(char)
            elif char in matching.values() and stack:
                val = stack.pop()
                if matching[val] != char:
                    return False
            elif char in matching.values() and not stack:
                return False
        if not stack:
            return True
        return False