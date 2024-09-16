class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,1,1,1,2,2,3,3,4]
        left = 0
        for right in nums[1: ]:
            if nums[left] != right:
                left += 1
                nums[left] = right
        return (left + 1)