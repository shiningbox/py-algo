class Heap:

    def __init__(self):
        pass

    '''
    one underscore as a private method
    Swap the element
    '''
    def _swap(self, idx, arr, length):
        min_idx = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < length and arr[left] < arr[min_idx]:
            min_idx = left

        if right < length and arr[right] < arr[min_idx]:
            min_idx = right

        # If child has the min value
        if min_idx != idx:
            # swap with child with min value
            arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
            # Continue with the min child
            self._swap(min_idx, arr, length)

    '''
    Heaplify the array in-place
    '''
    def heaplify(self, arr: []):
        # Make sure each subtree satisfy heap property
        # root <= left and root <= right
        # # last non leaf node = (n - 1 - 1) / 2 = n // 2 - 1
        n_len = len(arr)
        # Suppose the tree has n node, the last level is n / 2
        start_idx = n_len // 2 - 1
        # Starting with the last non-leaf node, heapify the array
        for i in range(start_idx, -1, -1):
            self._swap(i, arr, n_len)

    def heap_sort(self, arr:[]):
        self.heaplify(arr)
        l = len(arr)
        # then swap the root (min) to the last node (a large node)
        for i in range(l - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            # Now large node at the root node
            # Need to swap it down
            # make sure the any subtree satisfies the heap properties
            # and the last parts are sorted descending
            self._swap(0, arr, i)

    '''
    Pop the min element
    '''
    def heappop(self, arr: []):
        # pop the last node (min)
        # if you pop it n times then the array is sorted ascending
        return arr.pop()
