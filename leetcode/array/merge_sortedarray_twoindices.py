from typing import List
from typing import Optional

class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """

        # Move larger elements to the back

        # Move till one of the nums are empty
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        # if m > 0 and n == 0
        # nums2 are all placed
        # then just return nums1

        # if still elements in nums2
        # e.g., nums1= 4, nums2= 1 2 5 6
        # replace index = m + n - 1
        # 4 0 0 0 0     m = 1, n = 4,
        # 4 0 0 0 6     m = 1, n = 3
        # 4 0 0 5 6     m = 1, n = 2
        # 4 0 4 5 6     m = 0, n = 1

        # nums2[:2] = [1, 2]
        # nums1[:2] = [4, 0]

        # nums1 = [1, 2, 4 ,5 ,6]
        if n > 0:
            nums1[:n] = nums2[:n]

        print(nums1)


    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


    def merge_small(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if nums2 is None or len(nums2) == 0:
            return nums1[0:m]

        i = 0
        # Add nums in nums2 to nums1
        for j in range(m, m+n):
            nums1[j] = nums2[i]
            i += 1

        i = 0
        j = m
        # Compare and swap
        while i <= m - 1 and j <= m + n - 1:
            
            if nums1[i] > nums1[j]:
                # Swap
                self.swap(nums1, i, j)
                j += 1
            else:
                i += 1
        if j >= m + n:
            return nums1
        else:
            j = i
            while j + 1 <= m + n - 1:
                if nums1[j] > nums1[j + 1]:
                    # Swap
                    self.swap(nums1, j, j + 1)
                j += 1
        print(nums1)

def test():
    solution = Solution()
    # test method
    solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    solution.merge([1, 2, 3, 0, 0, 0, 0], 3, [1, 2, 5, 6], 4)
    solution.merge([1, 0], 1, [1], 1)
    solution.merge([0, 0, 0], 0, [1, 2, 3], 3)
    solution.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5)
    solution.merge([2, 0], 1, [1], 1)
    solution.merge([1, 2, 4, 5, 6, 0], 5, [3], 1)

test()
