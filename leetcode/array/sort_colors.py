from typing import List
from typing import Optional


def partition_array(l, h, array):
    l_i = l
    h_i = h - 1
    # scan until left_stack index meets right_stack index
    # Find smaller elements (less than pivot) that needs to be moved to left_stack sequence
    # Find larger elements (larger than pivot) that needs to be moved to right_stack sequence
    while l_i <= h_i:
        # Find the left_stack index that are larger than pivot, which needs to be swapped
        while l_i <= h_i and array[l_i] <= array[h]:
            l_i += 1
        # Find the right_stack index that are smaller than pivot, which needs to be swapped
        while l_i <= h_i and array[h_i] >= array[h]:
            h_i -= 1

        if l_i < h_i:
            # Swap left_stack index and right_stack index
            array[l_i], array[h_i] = array[h_i], array[l_i]
    # Swap the r_
    array[l_i], array[h] = array[h], array[l_i]
    return l_i

def quick_sort(l, h, array: list):
    # Find three sequences, L, P, R, bounded by 0, to Pivot -1, Pivot, Pivot + 1 to right_bound
    # Note that, L or R could be none, if less than 3
    # IF sequence size is 0 or 1
    if len(array) < 2:
        return
    if l >= h:
        return
    l_i = partition_array(l, h, array)
    # Sort left_stack sequence
    quick_sort(l, l_i - 1, array)
    quick_sort(l_i + 1, h, array)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        quick_sort(0, len(nums) -1, nums)

def test():
    solution = Solution()
    # test method
    print(solution.sortColors([2,0,2,1,1,0]))


test()
