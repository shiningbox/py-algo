from typing import List
from typing import Optional

# Divide and conquer
# Choose pivot
# Smaller ones on the left_stack
# Larger ones on the right_stack
# Fine-tune left_stack subarray and right_stack subarray
def partition(l, h, array):
    l_i = l
    h_i = h - 1
    # scan until left_stack index meets right_stack index
    # Find smaller elements (less than pivot) that needs to be moved to left_stack sequence
    # Find larger elements (larger than pivot) that needs to be moved to right_stack sequence
    while l_i <= h_i:
        # Find the left_stack index that are smaller than pivot, which needs to be swapped
        while l_i <= h_i and array[l_i] >= array[h]:
            l_i += 1
        # Find the right_stack index that are larger than pivot, which needs to be swapped
        while l_i <= h_i and array[h_i] <= array[h]:
            h_i -= 1

        if l_i < h_i:
            # Swap left_stack index and right_stack index
            array[l_i], array[h_i] = array[h_i], array[l_i]
    # Swap the r_
    array[l_i], array[h] = array[h], array[l_i]
    return l_i


def kth_largest(arr, l, r, k):

    # if k is smaller than number of
    # elements in array

    if 0 < k <= r - l + 1:

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(l, r, arr)

        # if position is same as k
        if index - l + 1 == k:
            return arr[index]

        # If position is more, recur
        # for left subarray
        if index - l + 1 > k:
            return kth_largest(arr, l, index - 1, k)

        # Else recur for right subarray
        return kth_largest(arr, index + 1, r,
                           k - (index - l + 1))

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return kth_largest(nums, 0, len(nums) - 1, k)


def test():
    solution = Solution()
    # test method
    arr = [3, 2, 1, 5, 6, 4]

    print(solution.findKthLargest(arr, 2))

test()
