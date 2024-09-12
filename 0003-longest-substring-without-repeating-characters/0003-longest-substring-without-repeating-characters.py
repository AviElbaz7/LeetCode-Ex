class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in longest_sub:
                longest_sub.remove(s[left])
                left+= 1
            longest_sub.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length