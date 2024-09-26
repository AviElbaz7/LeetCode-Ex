class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        hashmap = {}
        n = len(s)-1
        for i in range(len(s)):
            hashmap[n] = s[i]
            n -= 1
        
        for i in range(len(s)):
            s[i] = hashmap[i]