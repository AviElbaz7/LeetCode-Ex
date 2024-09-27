class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        for i in range(len(s)):
            hashmap = {}
            hashmap[s[i]] = 1
            for j in range(i + 1, len(s)):
                if s[j] in hashmap:
                    break
                hashmap[s[j]] = 1
            maxi = max(maxi, sum(hashmap.values()))
        return maxi