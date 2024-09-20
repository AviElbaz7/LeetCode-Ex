class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)
        def reverse(nums: List[int], start: int, end: int) -> List[int]:
            # if len(nums) == 1:
            #     return nums
            while(start < end):
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                start += 1
                end -= 1
            return nums
        nums = reverse(nums, 0, len(nums) - 1)
        nums = reverse(nums, 0, k - 1)
        nums = reverse(nums, k, len(nums) - 1)