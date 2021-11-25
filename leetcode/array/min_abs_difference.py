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

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # res arr to save the nums with min abs
        # if nums are larger than abs, continue
        # if nums are smaller than abs, then found new abs
        res_arr = []
        res_dict = {}
        self.quick_sort(0, len(arr) - 1, arr)
        min_abs = 10 ** 6

        i = 0
        j = 1
        # check 0,1, 1,2, 2,3...
        while j < len(arr):
            if abs(arr[j] - arr[i]) < min_abs:
                res_arr = [[arr[i], arr[j]]]
                min_abs = abs(arr[j] - arr[i])
            elif abs(arr[j] - arr[i]) == min_abs:
                res_arr.append([arr[i], arr[j]])
            i = j
            j += 1
        return res_arr

def test():
    solution = Solution()
    # test method
    print(solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))


test()
