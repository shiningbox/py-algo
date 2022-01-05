from typing import List
from typing import Optional

class Solution:

    def num_array(self, num):
        n_arr = []
        while num > 0:
            n_arr.insert(0, num % 10)
            num = num // 10
        return n_arr

    def array_num(self, arr):
        res = 0
        for i in range(len(arr))[::-1]:
            res += arr[i] * 10 ** (len(arr) - 1 - i)

        return res

    def maximumSwap(self, num: int) -> int:
        arr = self.num_array(num)
        rank_arr = set(arr)
        rank_arr = list(rank_arr)
        rank_arr.sort(reverse=True)
        min_arr = []

        min_r = rank_arr.index(arr[-1])

        for i in range(len(arr) - 1, -1, -1):
            if rank_arr.index(arr[i]) <= min_r:
                min_r = rank_arr.index(arr[i])
            min_arr.insert(0, min_r)

        count = 1

        for i in range(len(arr)):
            if count == 0:
                break
            min_r = rank_arr.index(arr[i])
            if rank_arr.index(arr[i]) > min_arr[i]:
                j = i + 1
                idx = j

                while j < len(arr):
                    if rank_arr.index(arr[j]) <= min_r:
                        min_r = rank_arr.index(arr[j])
                        idx = j
                    j += 1

                # swap
                arr[i], arr[idx] = arr[idx], arr[i]
                count = 0

        return self.array_num(arr)


def test():
    solution = Solution()
    # test method
    print(solution.maximumSwap(2736))
    print(solution.maximumSwap(9973))
    print(solution.maximumSwap(98368))
    print(solution.maximumSwap(99901))


test()
