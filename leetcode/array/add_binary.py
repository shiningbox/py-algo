from typing import List
from typing import Optional

class Solution:

    def make_equal(self, a: str, b: str):
        l1 = len(a)
        l2 = len(b)
        length = l1
        if l1 == l2:
            return l1, a, b

        if l1 > l2:
            length = l1

            for i in range(l1 - l2):
                b = '0' + b

        if l2 > l1:
            length = l2
            for i in range(l2 - l1):
                a = '0' + a

        return length, a, b

    def add_two_binary_digit(self, a, b, carry):
        # & and
        # | or
        # ^ XOR
        # ~ Not
        # << zero fill shift left_stack
        # >> zero fill shift right_stack
        # chr(48) = 0
        # chr(49) = 1
        sum = a ^ b ^ carry + 48
        car = (a & b) | (a & carry) | (b & carry)
        return car, sum

    def addBinary(self, a: str, b: str) -> str:
        length, a, b = self.make_equal(a, b)
        binaries = []
        carry = 0
        for i in range(length - 1, -1, -1):
            b_a = int(a[i])
            b_b = int(b[i])
            car, sum = self.add_two_binary_digit(b_a, b_b, carry)
            binaries.insert(0, chr(sum))
            carry = car

        if carry == 1:
            binaries = ['1'] + binaries

        return ''.join(binaries)

def test():
    solution = Solution()
    # test method
   # print(solution.addBinary("11", "1"))
   # print(solution.addBinary("111", "1"))
   # print(solution.addBinary("1010", "1011"))
    print(solution.addBinary("1", "111"))


test()
