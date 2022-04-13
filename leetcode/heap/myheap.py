class MinHeap:

    def __init__(self):
        pass

    '''
    Topdown to make sure the root of the tree if satisfied
    one underscore as a private method
    Swap the element
    '''
    def _topdown(self, idx, arr, length):
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
            self._topdown(min_idx, arr, length)

    '''
    Bottom up for inserting
    Insert the element to the end
    If parent is larger than end, swap with parent till root
    '''
    def _bottomup(self, idx, arr):
        min_idx = idx
        parent = idx // 2

        if parent >= 0 and arr[parent] > arr[min_idx]:
            min_idx = parent

        # If child has the min value
        if min_idx != idx:
            # swap with child with min value
            arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
            # Continue with the min child
            self._bottomup(min_idx, arr)

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
            self._topdown(i, arr, n_len)

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
            self._topdown(0, arr, i)

    '''
    Pop the min element
    '''
    def heappop(self, arr: []):
        n = len(arr)
        arr[n-1], arr[0] = arr[0], arr[n-1]
        # Top down to make sure the root satisfies heap properties
        res = arr.pop()
        n = len(arr)
        self._topdown(0, arr, n)
        return res

    def heappush(self, arr: [], num):
        # First add the num to the end of list
        arr.append(num)
        n = len(arr)
        # Then swap it to the first
        # Make sure root satisfy heap properties
        self._bottomup(n-1, arr)


class MaxHeap:

    def __init__(self):
        pass

    '''
    Topdown to make sure the root of the tree if satisfied
    one underscore as a private method
    Swap the element
    '''
    def _topdown(self, idx, arr, length):
        max_idx = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < length and arr[left] < arr[max_idx]:
            max_idx = left

        if right < length and arr[right] < arr[max_idx]:
            max_idx = right

        # If child has the min value
        if max_idx != idx:
            # swap with child with min value
            arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
            # Continue with the min child
            self._topdown(max_idx, arr, length)

    '''
    Bottom up for inserting
    Insert the element to the end
    If parent is larger than end, swap with parent till root
    '''
    def _bottomup(self, idx, arr):
        max_idx = idx
        parent = idx // 2

        if parent >= 0 and arr[parent] < arr[max_idx]:
            max_idx = parent

        # If child has the min value
        if max_idx != idx:
            # swap with child with min value
            arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
            # Continue with the min child
            self._bottomup(max_idx, arr)

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
            self._topdown(i, arr, n_len)

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
            self._topdown(0, arr, i)

    '''
    Pop the min element
    '''
    def heappop(self, arr: []):
        n = len(arr)
        arr[n-1], arr[0] = arr[0], arr[n-1]
        # Top down to make sure the root satisfies heap properties
        res = arr.pop()
        n = len(arr)
        self._topdown(0, arr, n)
        return res

    def heappush(self, arr: [], num):
        # First add the num to the end of list
        arr.append(num)
        n = len(arr)
        # Then swap it to the first
        # Make sure root satisfy heap properties
        self._bottomup(n-1, arr)