class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in val_index:
                return [i, val_index[temp]]
            else:
                val_index[nums[i]] = i