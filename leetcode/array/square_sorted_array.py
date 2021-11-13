from typing import List
from typing import Optional

class Solution:

    def calculate_squared_nums(self, nums):
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return nums

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        # Move larger elements to the back
        # Move till one of the nums is empty
        while m > 0 and n > 0:
            if abs(nums1[m - 1]) >= abs(nums2[n - 1]):
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

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find the sperator
        f_i = 0
        while f_i < len(nums) and nums[f_i] < 0:
            f_i += 1

        if f_i > 0:
            # re-order 0 to f_i
            i = 0
            j = f_i -1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            # Then swap 0 to f_i -1
            # and f_i to n
            nums1 = nums
            nums2 = nums[f_i:]
            self.merge(nums1, f_i, nums2, len(nums2))
        else:
            return self.calculate_squared_nums(nums)

        return self.calculate_squared_nums(nums1)



def test():
    solution = Solution()
    # test method
    print(solution.sortedSquares([-4,-1,0,3,10]))
    print(solution.sortedSquares([0,3,10, 12]))
    print(solution.sortedSquares([1,3,10, 12]))
    print(solution.sortedSquares([1]))
    print(solution.sortedSquares([-1]))
    print(solution.sortedSquares([-1, 0, 1]))
    print(solution.sortedSquares([-8, -4, 0, 1, 2]))


test()
