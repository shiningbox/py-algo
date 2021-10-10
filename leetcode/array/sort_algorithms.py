
# Divide and conquer
# Choose pivot
# Smaller ones on the left
# Larger ones on the right
# Fine-tune left subarray and right subarray
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


array = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
quick_sort(0, len(array) - 1, array)
print(array)
