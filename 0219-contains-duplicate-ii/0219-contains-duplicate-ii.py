class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for ind in range(len(nums)):
            if nums[ind] in hashmap:
                if abs(hashmap[nums[ind]] - ind) <= k:
                    return True

            hashmap[nums[ind]] = ind
        return False