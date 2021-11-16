from typing import List
from typing import Optional


class Solution:

    # heaplify the sub-tree rooted with node_idx
    def bottom_up(self, node_idx, n_len, nums):
        largest = node_idx
        left = node_idx * 2 + 1
        right = node_idx * 2 + 2

        # if left node is larger
        if left < n_len and nums[left] > nums[largest]:
            largest = left

        # if right node is larger
        if right < n_len and nums[right] > nums[largest]:
            largest = right

        # if one of the child has larger value, swap
        # and make the largest element is the root
        if largest != node_idx:
            nums[node_idx], nums[largest] = nums[largest], nums[node_idx]
            # Then make sure the sub-tree with the previous largest element, after swapped, satisfy heap properties
            self.bottom_up(largest, n_len, nums)

    # O(nlogn)
    def array_to_heap(self, nums):
        # last non leaf node = (n - 1 - 1) / 2 = n // 2 - 1
        n_len = len(nums)
        start_index = n_len // 2 - 1
        # build heap from last non-leaf node to root
        for node_idx in range(start_index, -1, -1):
            self.bottom_up(node_idx, n_len, nums)

    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        else:
            self.array_to_heap(stones)
            nlen = len(stones)
            for i in range(0, nlen - 1):
                print(stones)

                if stones[i] == 0:
                    continue

                if i < nlen - 2:
                    if stones[i + 1] <= stones[i + 2]:
                        stones[i + 2] = abs(stones[i] - stones[i + 2])
                        stones[i] = 0
                        self.bottom_up(i + 2, nlen, stones)
                    else:
                        stones[i + 1] = abs(stones[i] - stones[i + 1])
                        stones[i] = 0
                        self.bottom_up(i + 1, nlen, stones)
                else:
                    stones[i + 1] = abs(stones[i] - stones[i + 1])
                    stones[i] = 0
                    self.bottom_up(i + 1, nlen, stones)

        return stones[-1]


def test():
    solution = Solution()
    # test method
    print(solution.lastStoneWeight([2,7,4,1,8,1]))
    print(solution.lastStoneWeight([434,667,378,919,212,902,240,257,208,996,411,222,557,634,425,949,755,833,785,886,40,159,932,157,764,916,85,300,130,278]))

test()
