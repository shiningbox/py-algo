
# Divide and conquer
# Choose pivot
# Smaller ones on the left_stack
# Larger ones on the right_stack
# Fine-tune left_stack subarray and right_stack subarray
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


# Heap sort
# The element contained by each node is greater than or equal to the elements of that node's children.
# The tree is a complete binary tree.
# left_child = 2 * i + 1
# right_child = 2 * i + 2
# parent_node = (i-1) // 2

# heaplify the sub-tree rooted with node_idx
def bottom_up(node_idx, n_len, nums):
    largest = node_idx
    left = node_idx * 2 + 1
    right = node_idx * 2 + 2

    # if left_stack node is larger
    if left < n_len and nums[left] > nums[largest]:
        largest = left

    # if right_stack node is larger
    if right < n_len and nums[right] > nums[largest]:
        largest = right

    # if one of the child has larger value, swap
    # and make the largest element is the root
    if largest != node_idx:
        nums[node_idx], nums[largest] = nums[largest], nums[node_idx]
        # Then make sure the sub-tree with the previous largest element, after swapped, satisfy heap properties
        bottom_up(largest, n_len, nums)


# O(nlogn)
def array_to_heap(nums):
    # last non leaf node = (n - 1 - 1) / 2 = n // 2 - 1
    n_len = len(nums)
    start_index = n_len // 2 - 1
    # build heap from last non-leaf node to root
    for node_idx in range(start_index, -1, -1):
        bottom_up(node_idx, n_len, nums)


def heap_sort(nums):

    # first convert nums to heap
    array_to_heap(nums)
    l = len(nums)
    # then swap the root (largest) to the last node
    # One by one extract elements
    for i in range(l-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]  # swap
        # make sure the tree with root satisfies the heap properties
        bottom_up(0, i, nums)


array = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
quick_sort(0, len(array) - 1, array)
array2 = [1, 10, 8, 7, 3, 9, 6, 5, 2, 4]
heap_sort(array2)
print(array2)
