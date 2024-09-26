class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s)-1
        for i in range(int(len(s)/2)):
            temp = s[i]
            s[i] = s[right]
            s[right] = temp
            right -= 1