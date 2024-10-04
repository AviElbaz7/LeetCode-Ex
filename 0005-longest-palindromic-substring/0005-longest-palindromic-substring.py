class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest_poli = ""
        for i in range(n):
            odd_pali = expand_around_center(i, i)
            even_pali = expand_around_center(i, i +1)
            longest_poli = max(longest_poli, odd_pali, even_pali, key = len)
        return longest_poli