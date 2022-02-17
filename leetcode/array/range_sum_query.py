from typing import List
from typing import Optional


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        # Create and initialize BITree[] as 0
        self.bit = [0] * (self.n + 1)

        # Store the actual values in BITree[] using update()
        for i in range(self.n):
            self.update_bit(i, nums[i])

    def getsum(self, i):

        if i < 0:
            return 0

        s = 0  # initialize result

        # index in BITree[] is 1 more than the index in arr[]
        i = i + 1

        # Traverse ancestors of BITree[index]
        while i > 0:
            # Add current element of BITree to sum
            s += self.bit[i]
            i -= i & (-i)

        return s

    def update_bit(self, index: int, val: int) -> None:

        # index in BITree[] is 1 more than the index in arr[]
        index += 1

        # Traverse all ancestors and add 'val'
        while index <= self.n:
            # Add 'val' to current node of BI Tree
            self.bit[index] += val

            # Update index to that of parent in update View
            index += index & (-index)

    def update(self, index: int, val: int) -> None:

        self.nums[index] = val
        # Create and initialize BITree[] as 0
        self.bit = [0] * (self.n + 1)

        # Store the actual values in BITree[] using update()
        for i in range(self.n):
            self.update_bit(i, self.nums[i])


    def sumRange(self, left: int, right: int) -> int:
        return self.getsum(right) - self.getsum(left - 1)



obj = NumArray([1, 3, 5])
print(obj.sumRange(0, 2))
print(obj.update(1, 2))
print(obj.sumRange(0, 2))



