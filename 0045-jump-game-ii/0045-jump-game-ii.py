class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2, 3, 1, 2, 2, 1, 4]
        near, far, jump = 0, 0, 0
        while far < len(nums)-1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            near += 1
            far = farthest
            jump += 1
        return jump