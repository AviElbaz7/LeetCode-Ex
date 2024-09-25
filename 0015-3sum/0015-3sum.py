class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l1 = list()
        if len(nums) < 3 or nums == None:
            return []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[left]+ nums[right]
                if sum == 0:
                    l1.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return l1