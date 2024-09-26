class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {} # key = char, value = counter
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1