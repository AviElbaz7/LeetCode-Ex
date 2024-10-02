class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = 1
        counter = 0
        for i in range(32):
            if (a & (x ^ y) != 0):
                counter += 1
            a <<= 1
        return counter