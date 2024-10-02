class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sortedArr = []
        for i in range(0, len(nums)):
            index = self.BinarySearch(sortedArr, nums[i])
            if index >= len(sortedArr):
                sortedArr.append(nums[i])
            else:
                sortedArr[index] = nums[i]
        return len(sortedArr)


    def BinarySearch(self, sortedArr: List[int], target: int) -> int:
        left, right = 0, len(sortedArr)
        result = len(sortedArr)
        while left < right:
            mid = left + (right - left) // 2
            if sortedArr[mid] < target:
                left = mid + 1
            else:
                right = mid
                result = mid
        return result