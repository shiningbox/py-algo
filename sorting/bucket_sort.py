from list.array_sequence import ArraySequence

class BucketSort:
    CAPACITY = 1000

    def __init__(self):
        self.bucket_array = ArraySequence(BucketSort.CAPACITY)
        for index in range(BucketSort.CAPACITY):
            self.bucket_array.sequence[index] = ArraySequence(10)
            self.bucket_array.sequence_size += 1

    def sort(self, sequence: ArraySequence, key_index=0):
        seq_size = sequence.size()

        for index in range(seq_size):
            # Remove first
            tuple_elem = sequence.remove_elem_rank(0)
            # Insert the element with key to bucket[key]
            key = tuple_elem[key_index]
            bucket = self.bucket_array.elem_at_rank(key)
            bucket.insert_last(tuple_elem)

        for index, bucket in enumerate(self.bucket_array.sequence):
            if not bucket.is_empty():
                for i in range(bucket.size()):
                    tuple_elem = bucket.remove_elem_rank(0)
                    sequence.insert_last(tuple_elem)


def test():
    sequence = ArraySequence(100)
    tuple_element = (3, 3)
    sequence.insert_last(tuple_element)
    tuple_element = (1, 4)
    sequence.insert_last(tuple_element)
    tuple_element = (2, 5)
    sequence.insert_last(tuple_element)
    tuple_element = (1, 2)
    sequence.insert_last(tuple_element)
    tuple_element = (2, 3)
    sequence.insert_last(tuple_element)
    tuple_element = (1, 7)
    sequence.insert_last(tuple_element)
    tuple_element = (3, 2)
    sequence.insert_last(tuple_element)
    tuple_element = (2, 2)
    sequence.insert_last(tuple_element)
    sequence.print()

    bucket_sort = BucketSort()
    bucket_sort.sort(sequence, 1)
    bucket_sort.sort(sequence, 0)
    print(f"Sorted...")
    sequence.print()


test()



