class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # [2,2]
        #  l
        # [1,1,2,2]
        #  r
        nums1.sort()
        nums2.sort()
        if len(nums2) <= len(nums1):
            nums1, nums2 = nums2, nums1
        l1 = list()
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                l1.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                l += 1
        return l1
            