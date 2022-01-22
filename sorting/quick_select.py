from list.array_sequence import ArraySequence
import random

class QuickSelect:

    def __init__(self):
        pass

    @staticmethod
    def select_k(k: int, seq: ArraySequence):

        size = seq.size()
        print(size)
        if seq.size() == 1:
            return seq.elem_at_rank(0)

        # Random select a pivot point
        index = random.choice(range(0, size))
        pivot = seq.elem_at_rank(index)
        l_seq = ArraySequence(15)
        e_seq = ArraySequence(10)
        g_seq = ArraySequence(10)
        # Split the sequence into three
        while not seq.is_empty():
            element = seq.remove_elem_rank(0)
            if element < pivot:
                l_seq.insert_last(element)
            elif element == pivot:
                e_seq.insert_last(element)
            else:
                g_seq.insert_last(element)

        # Select K in the L sequence
        if k <= l_seq.size():
            return QuickSelect.select_k(k, l_seq)

        # Return the pivot
        elif k <= l_seq.size() + e_seq.size():
            return pivot
        else:
            return QuickSelect.select_k(k - (l_seq.size() + e_seq.size()), g_seq)


array = ArraySequence(100)
array.insert_last(85)
array.insert_last(24)
array.insert_last(24)
array.insert_last(63)
array.insert_last(45)
array.insert_last(17)
array.insert_last(31)
array.insert_last(96)
array.insert_last(50)
array.insert_last(32)
# 17, 24, 31, 32, 45, 50, 63, 85, 96
result = QuickSelect.select_k(2, array)
print(result)









