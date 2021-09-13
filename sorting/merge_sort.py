from list.linked_sequence import LinkedSequence
import math

class ListMergeSort:

    def __init__(self):
        pass

    def sort(self, sequence: LinkedSequence):

        # If the sequence has only one element, return it as the end of recursion call
        if sequence.size() < 2:
            return

        # Divide and conquer
        seq1, seq2 = self.divide_seq(sequence)

        # Sort the first sequence
        self.sort(seq1)
        # Sort the second sequence
        self.sort(seq2)
        # Merge seq1 and seq2
        self.merge(seq1, seq2, sequence)

    def divide_seq(self, sequence: LinkedSequence):
        seq1 = LinkedSequence()
        seq2 = LinkedSequence()
        break_point = math.ceil(sequence.size() / 2)
        end_point = sequence.size()
        for i in range(break_point):
            seq1.insert_last(sequence.remove(sequence.first()))
        for i in range(break_point, end_point):
            seq2.insert_last(sequence.remove(sequence.first()))
        return seq1, seq2

    def merge(self, seq1: LinkedSequence, seq2: LinkedSequence, seq: LinkedSequence):
        # Insert the smallest elements to sequence, starting from first
        while not seq1.is_empty() and not seq2.is_empty():
            if seq1.first().element <= seq2.first().element:
                seq.insert_last(seq1.remove(seq1.first()))
            else:
                seq.insert_last(seq2.remove(seq2.first()))
        # If seq1 still has elements
        if seq2.is_empty():
            while not seq1.is_empty():
                seq.insert_last(seq1.remove(seq1.first()))
        # If seq2 still has elements
        if seq1.is_empty():
            while not seq2.is_empty():
                seq.insert_last(seq2.remove(seq2.first()))
        

seq = LinkedSequence()
seq.insert_last(1)
seq.insert_last(24)
seq.insert_last(56)
seq.insert_last(6)
seq.insert_last(12)
seq.insert_last(2)
seq.insert_last(2)
seq.insert_last(10)
seq.insert_last(9)
seq.insert_last(4)
seq.insert_last(78)
merge_sort = ListMergeSort()
merge_sort.sort(seq)

