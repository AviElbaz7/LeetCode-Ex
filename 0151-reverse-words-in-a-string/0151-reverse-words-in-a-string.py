class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        res = []
        for i in range(len(words) - 1, -1, -1):
            if words[i]:
                res.append(words[i])
        ans = ' '.join(res)
        return ans