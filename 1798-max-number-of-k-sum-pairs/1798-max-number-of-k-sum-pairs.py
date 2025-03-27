from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        res = 0

        for num in nums:
            if freq[num] > 0 and freq.get(k - num, 0) > 0:  # לבדוק אם קיים צמד
                if num == k - num and freq[num] < 2:  # מונע שימוש יתר במספר זהה
                    continue
                res += 1
                freq[num] -= 1
                freq[k - num] -= 1

        return res
