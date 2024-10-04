class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pali = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i: j+1]
                if substring == substring[::-1] and len(substring) > len(max_pali):
                    max_pali = substring
        return max_pali