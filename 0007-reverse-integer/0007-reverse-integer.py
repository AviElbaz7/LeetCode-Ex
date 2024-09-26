class Solution:
    def reverse(self, x: int) -> int:
        # 123
        # 3
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            remainder = x % 10
            result = (result * 10) + remainder
            if result > 2**31:
                return 0
            x = x // 10
        return sign * result