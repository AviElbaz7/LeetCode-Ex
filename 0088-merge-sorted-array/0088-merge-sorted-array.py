class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        n2pointer = n - 1
        n1pointer = m - 1
        while n2pointer >= 0:
            if n1pointer >= 0 and nums1[n1pointer] > nums2[n2pointer]:
                nums1[last] = nums1[n1pointer]
                n1pointer -= 1
                last -= 1
            else:
                nums1[last] = nums2[n2pointer]
                n2pointer -= 1
                last -= 1
        return None