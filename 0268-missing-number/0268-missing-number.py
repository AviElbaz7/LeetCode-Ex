class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashtable = {}
        for num in nums:
            hashtable[num] = 1
        maxi = max(nums)
        mini = min(nums)
        for i in range(mini, maxi + 1):
            if i not in hashtable:
                return i
        if 0 not in hashtable:
            return 0
        return len(nums)