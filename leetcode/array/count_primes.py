from typing import List
from typing import Optional

class Solution:

    def is_prime(self, n):
        if n <= 1:
            return False

        for i in range(2, n):
            # n / i <= i
            # Only consider factors up to √n because,
            # if n is divisible by some number p, then n = p × q and
            # since p ≤ q, we could derive that p ≤ √n.
            if i ** 2 > n:
                break

            if n % i == 0:
                return False

        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            if self.is_prime(i):
                count += 1
                print(i)
        return count

def test():
    solution = Solution()
    # test method
    print(solution.countPrimes(10))


test()
