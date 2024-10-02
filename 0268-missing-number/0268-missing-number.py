class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = (len(nums) * (len(nums) + 1)) // 2
        total = sum(nums)
        
        return sum_nums - total