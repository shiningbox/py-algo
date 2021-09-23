from typing import List
from typing import Optional


digits = 8

class Solution:
    # example:
    # n = 01110101
    # n & 1 means the digits of last index
    # res = 0 << 1 = 0, n = 01110101, res = 0 | 1 = 1
    # n = 01110101 >> 1 = 00111010

    # res = 10, n = 00111010, res = 10 | 0 = 10
    # n = 00111010 >> 1 = 00011101

    # res = 100, n = 00011101, res = 100 | 1 = 101
    # n = 00001110

    # res = 1010, n = 00001101 res = 1010 | 0 = 1010
    # n = 00000111

    # res = 10100, n = 00000111, res = 10100 | 1 = 10101
    # n = 00000011

    # res = 101010, n = 00000011, res = 101010 | 1 = 101011
    # n = 00000001

    # res = 1010110, n = 00000001, res = 1010110 | 1 = 1010111
    # n = 00000000

    # res = 1010111, n = 00000000, res = 10101110 | 0 = 10101110
    # n = 00000000

    def reverseBits(self, n):
        res = 0
        for i in range(digits):
            # Move res to left to receive digits from n last
            # like append the last digit of n to first digit of res
            res = (res << 1) | (n & 1)
            # remove the last digit of n
            n >>= 1
        return res


def test():
    solution = Solution()
    # test method
    # 43261596
    # 00000010100101000001111010011100
    # 117
    # 01110101
    print(solution.reverseBits(117))
    # 4294967293
    # 11111111111111111111111111111101
    # print(solution.reverseBits(4294967293))

test()
