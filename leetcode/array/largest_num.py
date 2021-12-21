from typing import List
from typing import Optional

class Solution:

    def compare_le(self, a, b):

        if not a and not b:
            return True

        if ord(a[0]) < ord(b[0]):
            return True
        elif ord(a[0]) > ord(b[0]):
            return False
        else:
            return self.compare_le(a[1:], b[1:])

    def merge(self, seq1, seq2):

        # Merge two sorted list
        seq = []
        while seq1 and seq2:
            a = seq1[0] + seq2[0]
            b = seq2[0] + seq1[0]
            if not self.compare_le(a, b):
                top = seq1.pop(0)
                seq.append(top)
            else:
                top = seq2.pop(0)
                seq.append(top)
        if not seq1:
            seq += seq2
        if not seq2:
            seq += seq1
        return seq

    # merge sorting
    def merge_sort(self, strs):

        # If the sequence has only one element,
        # return it as the end of recursion call

        if len(strs) < 2:
            return strs

        # Divide
        seq1, seq2 = strs[:len(strs) // 2], strs[len(strs) // 2:]

        # Conquer: sort the first sequence
        sorted_seq1 = self.merge_sort(seq1)

        # Conquer: sort the second sequence
        sorted_seq2 = self.merge_sort(seq2)

        # Merge: merge seq1 and seq2
        return self.merge(sorted_seq1, sorted_seq2)

    def largestNumber(self, nums: List[int]) -> str:
        str_array = [str(num) for num in nums]
        if len(str_array) < 2:
            return ''.join(str_array)

        sorted_strs = self.merge_sort(str_array)

        # Remove heading zeros
        i = 0
        while sorted_strs[i] == "0" and i < len(sorted_strs) - 1:
            i += 1

        return ''.join(sorted_strs[i:])

def test():
    solution = Solution()
    # test method

    #print(solution.largestNumber([1]))
    print(solution.largestNumber([34,5,9,3,30]))
    print(solution.largestNumber([34323,3432]))
    print(solution.largestNumber([111311, 1113]))
    print(solution.largestNumber([8308, 8308, 830]))
    print(solution.largestNumber([0, 0]))
    print(solution.largestNumber([0, 0, 0]))
    print(solution.largestNumber([0]))
    print(solution.largestNumber([1, 1, 1]))

test()
