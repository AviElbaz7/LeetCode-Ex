class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            remainder = x % 10
            result = (result * 10) + remainder
            if result > 2**31 - 1:
                return 0
            x = x // 10
        return sign * result