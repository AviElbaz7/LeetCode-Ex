class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dicti = {}
        res = 0
        for n in nums:
            if n in dicti:
                dicti[n] += 1
            else:
                dicti[n] = 1
        
        for n in nums:
            if dicti.get(n, 0) == 0:
                continue
            if dicti.get(k - n, 0) == 0:
                continue
            if (k - n) == n and dicti[n] < 2:
                continue
            res += 1
            dicti[n] -= 1
            dicti[k - n] -= 1
        return res