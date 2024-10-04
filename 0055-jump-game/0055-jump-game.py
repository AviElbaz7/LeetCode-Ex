class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # Farthest position we can reach so far
        for i in range(len(nums)):
            if i > farthest:
                # If we are at a position beyond the farthest point we can reach, we can't proceed
                return False
            # Update the farthest point we can reach from this position
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                # If we can reach or exceed the last index, return True
                return True
        return True
