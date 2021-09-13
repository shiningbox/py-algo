from typing import List
from typing import Optional

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n)
        l = len(nums)
        if l <= 1:
            return l
        # Unique index
        ui = 0
        for i in range(1, l):
            if nums[i] != nums[ui]:
                ui += 1
                nums[ui] = nums[i]
                i += 1
            else:
                i += 1
        return ui + 1


    def removeDuplicates_n2(self, nums: List[int]) -> int:
        # O(n ** 2)
        i = 0
        l = len(nums)

        if l == 0 or l == 1:
            return l

        duplicated = 0
        while i <= l - 1:
            if nums[i] == -1999:
                i += 1
                continue
            ui = i + 1
            # Marked all duplicated as 0
            # 0  1  2  3 4 ...
            # 1 -1 -1 -1 3 ...

            while ui < l and nums[i] == nums[ui]:
                nums[ui] = -1999
                ui += 1
                duplicated += 1
            # Duplicated window
            w = ui - i - 1
            # i  1  2 ui
            # 1 -1 -1 2 ...
            # Jump forward
            # If there are some duplicated values after i
            # Then move the marked `-1`s to the end of the array

            if w > 0:
                for j in range(ui, l):
                    temp = nums[j - w]
                    nums[j - w] = nums[j]
                    nums[j] = temp

            i += 1

        return l - duplicated



def test():
    solution = Solution()
    # test method
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([1]))
    print(solution.removeDuplicates([]))
    print(solution.removeDuplicates([1, 1]))
    print(solution.removeDuplicates([-100, -100, -100, -100, -99, -99, -99, -99]))
    print(solution.removeDuplicates([1, 2]))
    print(solution.removeDuplicates([-3, -1, -1, 0, 0, 0, 0, 0, 2]))



test()
