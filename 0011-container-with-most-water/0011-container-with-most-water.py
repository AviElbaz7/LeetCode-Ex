class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_con = 0
        l, r = 0, len(height) - 1
        while l < r:
            cur_con = (r - l) * min(height[l], height[r])
            max_con = max(max_con, cur_con)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_con