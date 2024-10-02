class Solution:
    def reverseBits(self, n: int) -> int:
        # n =    00000010100101000001111010011100
        # a =    00000000000000000000000000000001
        # num =  00000000000000000000000000000000
        a = 1
        num = 0
        for i in range(32):
            if (a & n) != 0:
                num += a
            n >>= 1
            num <<= 1
        num >>= 1
        return num