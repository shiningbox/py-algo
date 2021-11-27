from typing import List
from typing import Optional


def quick_sort(l, r, array: list):
    # Find three sequences, L, P, R, bounded by 0, to Pivot -1, Pivot, Pivot + 1 to right_bound
    # Note that, L or R could be none, if less than 3
    # IF sequence size is 0 or 1
    if len(array) < 2:
        return

    if l >= r :
        return

    p = array[r]
    l_i = l
    r_i = r - 1
    # scan until left_stack index meets right_stack index
    # Find smaller elements (less than pivot) that needs to be moved to left_stack sequence
    # Find larger elements (larger than pivot) that needs to be moved to right_stack sequence
    while l_i <= r_i:
        # Find the left_stack index that are larger than pivot, which needs to be swapped
        while l_i <= r_i and array[l_i] <= p:
            l_i += 1
        # Find the right_stack index that are smaller than pivot, which needs to be swapped
        while l_i <= r_i and array[r_i] >= p:
            r_i -= 1
        if l_i < r_i:
            # Swap left_stack index and right_stack index
            temp = array[l_i]
            array[l_i] = array[r_i]
            array[r_i] = temp
    # Swap the r_
    temp = array[l_i]
    array[l_i] = array[r]
    array[r] = temp
    # Sort left_stack sequence
    quick_sort(l, l_i - 1, array)
    quick_sort(l_i + 1, r, array)

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Sort the nums
        offset_dict = {}
        for i in range(len(nums)):
            if nums[i] not in offset_dict:
                offset_array = [i]
                offset_dict[nums[i]] = offset_array
            else:
                offset_array = offset_dict[nums[i]]
                offset_array.append(i)
        max_seq = 0

        for num in nums:
            prev_seq = 0
            after_seq = 0
            s = offset_dict[num][0]
            e = offset_dict[num][-1]
            if num - 1 in offset_dict:
                prev_seq += len(offset_dict[num - 1])

            if num + 1 in offset_dict:
                after_seq += len(offset_dict[num + 1])

            seq = max(prev_seq, after_seq)

            if seq > 0:
                seq += len(offset_dict[num])

            if seq >= max_seq:
                max_seq = seq

        return max_seq

def test():
    solution = Solution()
    # test method
    print(solution.findLHS([1]))
    print(solution.findLHS([1,1,1,1]))
    print(solution.findLHS([1,2,2]))
    print(solution.findLHS([1,3,2,2,5,2,3,7]))
    print(solution.findLHS([1,2,3,4]))


test()
