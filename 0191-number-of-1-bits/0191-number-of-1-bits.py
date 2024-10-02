class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 1
        counter = 0
        for i in range(32):
            if (n & a) != 0:
                counter += 1
            a *= 2

        return counter