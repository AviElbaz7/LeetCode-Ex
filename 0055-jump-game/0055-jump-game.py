class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        near, far = 0, 0
        while far < len(nums):
            # far = 1, near = 1, farthest = 0
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
            if farthest == far:
                return False
            far = farthest
            near += 1
        return True