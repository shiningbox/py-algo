from typing import List
from typing import Optional


class Solution:

    def quick_sort(self, l, r, array: list):
        # Find three sequences, L, P, R, bounded by 0, to Pivot -1, Pivot, Pivot + 1 to right_bound
        # Note that, L or R could be none, if less than 3
        # IF sequence size is 0 or 1
        if len(array) < 2:
            return

        if l >= r:
            return

        p = array[r]
        l_i = l
        r_i = r - 1
        # scan until left index meets right index
        # Find smaller elements (less than pivot) that needs to be moved to left sequence
        # Find larger elements (larger than pivot) that needs to be moved to right sequence
        while l_i <= r_i:
            # Find the left index that are larger than pivot, which needs to be swapped
            while l_i <= r_i and array[l_i] <= p:
                l_i += 1
            # Find the right index that are smaller than pivot, which needs to be swapped
            while l_i <= r_i and array[r_i] >= p:
                r_i -= 1
            if l_i < r_i:
                # Swap left index and right index
                temp = array[l_i]
                array[l_i] = array[r_i]
                array[r_i] = temp
        # Swap the r_
        temp = array[l_i]
        array[l_i] = array[r]
        array[r] = temp
        # Sort left sequence
        self.quick_sort(l, l_i - 1, array)
        self.quick_sort(l_i + 1, r, array)

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_dict = {}
        i = 0

        while i < len(arr2):
            arr_dict[arr2[i]] = i
            i += 1

        i = 0
        nums1 = []
        nums2 = []
        while i < len(arr1):
            if arr1[i] in arr_dict:
                nums1.append(arr_dict[arr1[i]])
            else:
                nums2.append(arr1[i])
            i += 1
        self.quick_sort(0, len(nums1) - 1, nums1)
        self.quick_sort(0, len(nums2) - 1, nums2)

        # Convert nums1 back
        i = 0

        while i < len(nums1):
            nums1[i] = arr2[nums1[i]]
            i += 1

        return nums1 + nums2

def test():
    solution = Solution()
    # test method
    print(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))


test()
