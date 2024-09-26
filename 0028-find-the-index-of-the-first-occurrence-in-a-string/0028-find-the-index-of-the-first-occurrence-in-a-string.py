class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 1:
            for char in range(len(haystack)):
                if haystack[char] == needle:
                    return char
        if len(needle) == len(haystack) and haystack == needle:
            return 0
        counter = 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                counter += 1
                for j in range(1, len(needle)):
                    if haystack[i + j] == needle[j]:
                        counter += 1
                if counter == len(needle):
                    return i
                counter = 0
        return -1