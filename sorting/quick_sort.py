from list.array_sequence import ArraySequence

class QuickSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(left_bound, right_bound, sequence: ArraySequence):

        # Find three sequences, L, P, R, bounded by 0, to Pivot -1, Pivot, Pivot + 1 to right_bound
        # Note that, L or R could be none, if less than 3
        # IF sequence size is 0 or 1
        if sequence.size() < 2:
            return

        if left_bound >= right_bound:
            return

        pivot_elem = sequence.elem_at_rank(right_bound)
        left_index = left_bound
        right_index = right_bound - 1
        # scan until left_stack index meets right_stack index
        # Find smaller elements (less than pivot) that needs to be moved to left_stack sequence
        # Find larger elements (larger than pivot) that needs to be moved to right_stack sequence
        while left_index <= right_index:
            # Find the left_stack index that are larger than pivot, which needs to be swapped
            while left_index <= right_index and sequence.elem_at_rank(left_index) <= pivot_elem:
                left_index += 1
            # Find the right_stack index that are smaller than pivot, which needs to be swapped
            while right_index >= left_index and sequence.elem_at_rank(right_index) >= pivot_elem:
                right_index -= 1
            if left_index < right_index:
                # Swap left_stack index and right_stack index
                sequence.swap(left_index, right_index)
        sequence.swap(left_index, right_bound)
        # Sort left_stack sequence
        QuickSort.sort(left_bound, left_index-1, sequence)
        QuickSort.sort(left_index+1, right_bound, sequence)


array = ArraySequence(100)
array.insert_last(85)
array.insert_last(24)
array.insert_last(63)
array.insert_last(45)
array.insert_last(17)
array.insert_last(31)
array.insert_last(96)
array.insert_last(50)
QuickSort.sort(0, array.size() - 1, array)
array.print()









