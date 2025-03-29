class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapper = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

        res = []

        def dfs(i, path):
            if i == len(digits):
                res.append(''.join(path))
                return
            
            for letter in mapper[digits[i]]:
                dfs(i + 1, path + [letter])

        dfs(0, [])
        return res