from typing import List
from typing import Optional

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



class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = score.copy()
        # first convert nums to heap
        array_to_heap(sorted_score)
        l = len(score)
        results_dict = {}
        results = []
        # then swap the root (largest) to the last node
        # One by one extract elements
        for i in range(l - 1, -1, -1):

            if len(results_dict.keys()) == 0:
                results_dict[sorted_score[0]] = "Gold Medal"
            elif len(results_dict.keys()) == 1:
                results_dict[sorted_score[0]] = "Silver Medal"
            elif len(results_dict.keys()) == 2:
                results_dict[sorted_score[0]] = "Bronze Medal"
            else:
                results_dict[sorted_score[0]] = str(len(results_dict.keys()) + 1)

            sorted_score[i], sorted_score[0] = sorted_score[0], sorted_score[i]  # swap
            # make sure the tree with root satisfies the heap properties
            bottom_up(0, i, sorted_score)

        for num in score:
            results.append(results_dict[num])

        return results

def test():
    solution = Solution()
    # test method
    print(solution.findRelativeRanks([5,4,3,2,1]))
    print(solution.findRelativeRanks([10,3,8,9,4]))


test()
