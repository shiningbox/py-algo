import heapq as heap
from myheap import Heap
import unittest

'''
Example of a min heap
[1, 5, 2, 6, 3, 4] - > [1, 3, 2, 6, 5, 4]
   1
 3   2
6 5 4  8
'''

arr = [1, 5, 2, 6, 3, 4, 8]
arr2 = [1, 5, 2, 6, 3, 4, 8]
# 5, 2, 9
print(f"Before heapify {arr}")
heap.heapify(arr)
heap2 = Heap()
heap2.heaplify(arr2)
print(f"After heapify")
print(arr)
print(arr2)

print("Sorting arr 2 descending")
heap2.heap_sort(arr2)
print(arr2)
for i in range(len(arr)):
    print(heap.heappop(arr), end="-")
print("")
for i in range(len(arr2)):
    print(heap2.heappop(arr2), end="-")
