class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left_to_right = [1] * len(nums)
        right_to_left = [1] * len(nums)

        for i in range(1, len(nums)):
            left_to_right[i] = (left_to_right[i - 1] * nums[i - 1])
        for i in range(len(nums)-2, -1, -1):
            right_to_left[i] = (right_to_left[i + 1] * nums[i + 1])
        for i in range(len(nums)):
            res[i] = left_to_right[i] * right_to_left[i]
        return res