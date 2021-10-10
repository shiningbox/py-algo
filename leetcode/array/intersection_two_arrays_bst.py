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
    quick_sort(l, l_i - 1, array)
    quick_sort(l_i + 1, r, array)


class TreeNode:
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val
        self.returned = False

def convert_array_bst(nums, l, h):
    if l > h:
        return None
    mid = (l + h) // 2
    root = TreeNode(None, None, nums[mid])
    root.left = convert_array_bst(nums, l, mid-1)
    root.right = convert_array_bst(nums, mid+1, h)
    return root

def binary_search(root, t):
    if not root:
        return None

    if root.left and not root.left.returned and root.left.val == t:
        root.left.returned = True
        return root.left.val

    if root.right and not root.right.returned and root.right.val == t:
        root.right.returned = True
        return root.right.val


    # If this node is already been visited
    if root.returned:
        if t < root.val:
            return binary_search(root.left, t)
        else:
            return binary_search(root.right, t)

    if not root.returned and root.val == t:
        root.returned = True
        return root.val


    if t < root.val:
        if root.left:
            return binary_search(root.left, t)
    else:
        if root.right:
            return binary_search(root.right, t)

    return None

class Solution:

    def find_inserct(self, nums1, nums2):
        results = []
        root = convert_array_bst(nums1, 0, len(nums1) - 1)
        for num in nums2:
            res = binary_search(root, num)
            if res is not None:
                results.append(res)
        return results

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) >= len(nums2):
            quick_sort(0, len(nums1) - 1, nums1)
            return self.find_inserct(nums1, nums2)
        else:
            quick_sort(0, len(nums2)-1, nums2)
            return self.find_inserct(nums2, nums1)


def test():
    solution = Solution()
    # test method
    print(solution.intersect([1, 2, 2, 1], [2, 2]))
    print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(solution.intersect([1], [0]))
    print(solution.intersect([1], [1]))
    print(solution.intersect([1, 2], [1, 1]))
    print(solution.intersect([1, 2], [1, 2]))
    print(solution.intersect([1, 2], [1, 1, 1]))
    print(solution.intersect([1, 2, 2, 1], [1, 1]))
    print(solution.intersect([8, 0, 3], [0, 0]))


test()
