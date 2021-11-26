from typing import List
from typing import Optional


class Solution:

    def quick_sort(self, l, r, array: list):
        # Find three sequences, L, P, R, bounded by 0, to Pivot -1, Pivot, Pivot + 1 to right_bound
        # Note that, L or R could be none, if less than 3
        # IF sequence size is 0 or 1
        if len(array) < 2:
            return

        if l >= r:
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
        self.quick_sort(l, l_i - 1, array)
        self.quick_sort(l_i + 1, r, array)

    def hash_valus(self, nums):
        result = 0
        for j in range(len(nums)):
            result += 2 ** nums[j]
        return result + 31

    def twoSum(self, index, numbers: List[int], results, visited_dict):
        i = 0
        j = len(numbers) - 1
        while i < j:
            # skip index
            if i == index:
                i += 1
                continue
            if j == index:
                j -= 1
                continue
            target = -1 * numbers[index]
            if numbers[i] + numbers[j] == -1 * numbers[index]:
                hashed_value = self.hash_valus([numbers[index], numbers[i], numbers[j]])
                if hashed_value not in visited_dict:
                    results.append([numbers[index], numbers[i], numbers[j]])
                    visited_dict[hashed_value] = 1
                i += 1
                j -= 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.quick_sort(0, len(nums)-1, nums)
        results = []
        visited_dict = {}
        if len(nums) < 3:
            return []
        else:
            if nums.count(0) == len(nums):
                return [[0, 0, 0]]
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] >= 0:
                    self.twoSum(j, nums, results, visited_dict)

        return results

def test():
    solution = Solution()
    # test method
    print(solution.threeSum([-2, 1, 1]))
    print(solution.threeSum([]))
    print(solution.threeSum([0]))
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0, 0, 0]))
    print(solution.threeSum([0, 0, 0, 0]))
    print(solution.threeSum([-1,0,1,0]))
    print(solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))

test()
