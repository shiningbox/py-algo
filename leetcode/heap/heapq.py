import heapq as heap
from myheap import MinHeap
import unittest

'''
Example of a min heap
[1, 5, 2, 6, 3, 4] - > [1, 3, 2, 6, 5, 4]
   1
 3   2
6 5 4  8
'''

min_heap = MinHeap()

def test_heaplify():
    arr = [1, 5, 2, 6, 3, 4, 8]
    arr2 = [1, 5, 2, 6, 3, 4, 8]
    # 5, 2, 9
    print(f"Before heapify {arr}")
    heap.heapify(arr)
    print(f"After heapify")
    print(arr)
    print(arr2)
    print("Sorting arr 2 descending")
    min_heap.heap_sort(arr2)
    print(arr2)

def test_push_pop():
    arr = [1, 5, 2, 6, 3, 4, 8]
    heap1 = []
    heap2 = []
    for num in arr:
        heap.heappush(heap1, num)
        min_heap.heappush(heap2, num)
    print(heap1)
    print(heap2)

    for i in range(len(arr)):
        print(heap.heappop(heap1), end="-")
    print("\n")
    for i in range(len(arr)):
        print(min_heap.heappop(heap2), end="-")

test_push_pop()
