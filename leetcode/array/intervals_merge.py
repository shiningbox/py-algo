from typing import List
from typing import Optional

class Solution:

    def partition_array(self, l, h, array):
        l_i = l
        h_i = h - 1
        # scan until left_stack index meets right_stack index
        # Find smaller elements (less than pivot) that needs to be moved to left_stack sequence
        # Find larger elements (larger than pivot) that needs to be moved to right_stack sequence
        while l_i <= h_i:
            # Find the left_stack index that are larger than pivot, which needs to be swapped
            while l_i <= h_i and array[l_i][0] <= array[h][0]:
                l_i += 1
            # Find the right_stack index that are smaller than pivot, which needs to be swapped
            while l_i <= h_i and array[h_i][0] >= array[h][0]:
                h_i -= 1

            if l_i < h_i:
                # Swap left_stack index and right_stack index
                array[l_i], array[h_i] = array[h_i], array[l_i]
        # Swap the r_
        array[l_i], array[h] = array[h], array[l_i]
        return l_i

    def quick_sort(self, l, h, array: list):
        # Find three sequences, L, P, R, bounded by 0, to Pivot -1, Pivot, Pivot + 1 to right_bound
        # Note that, L or R could be none, if less than 3
        # IF sequence size is 0 or 1
        if len(array) < 2:
            return
        if l >= h:
            return

        l_i = self.partition_array(l, h, array)
        # Sort left_stack sequence
        self.quick_sort(l, l_i - 1, array)
        self.quick_sort(l_i + 1, h, array)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        self.quick_sort(0, len(intervals) - 1, intervals)
        res = [intervals[0]]
        i = 0
        j = 1

        while j < len(intervals):
            #print(res, i, j)
            if res[i][1] < intervals[j][0] and res[i][1] < intervals[j][1]:
                res.append(intervals[j])
                i += 1
                j += 1
            else:
                if intervals[j][1] > res[i][1]:
                    res[i] = [res[i][0], intervals[j][1]]
                j += 1

        return res

def test():
    solution = Solution()
    # test method
    print(solution.merge([[1,3], [8,10], [2,6],  [15,18]]))
    print(solution.merge([[1,3]]))
    print(solution.merge([[1, 4], [1, 5]]))
    print(solution.merge([[1,4], [5, 6]]))
    print(solution.merge([[1, 4], [2, 3]]))


test()
