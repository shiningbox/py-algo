from typing import List

class Solution:

    def min(self, strs: List[str]) -> int:
        min_len = len(strs[0])
        for str in strs:
            if len(str) <= min_len:
                min_len = len(str)
        return min_len

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # O(mn)
        str_lens = len(strs)

        if str_lens == 1:
            return strs[0]

        first_string = strs[0]

        min_len = self.min(strs)
        count = 0
        for i in range(min_len):
            equal = True
            land_char = first_string[i]
            for j in range(1, str_lens):
                if strs[j][i] != land_char:
                    equal = False

            if equal:
                count += 1
            else:
                break

        if count > 0:
            return first_string[0:count]
        else:
            return ""

def test():
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))

    # test method


test()
