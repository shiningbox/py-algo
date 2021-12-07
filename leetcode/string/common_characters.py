from typing import List
from typing import Optional

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_count_dict = {}

        for char in words[0]:
            if char not in min_count_dict:
                min_count_dict[char] = 1
            else:
                min_count_dict[char] += 1
        res = []

        for i in range(1, len(words)):

            temp_dict = {}

            for char in words[i]:
                if char not in temp_dict:
                    temp_dict[char] = 1
                else:
                    temp_dict[char] += 1

            for key, value in min_count_dict.items():
                if key in temp_dict:
                    if temp_dict[key] <= min_count_dict[key]:
                        min_count_dict[key] = temp_dict[key]
                else:
                    min_count_dict[key] = 0

        for key, value in min_count_dict.items():
            if value > 0:
                for i in range(value):
                    res.append(key)

        return res


def test():
    solution = Solution()
    # test method
    print(solution.commonChars(["a"]))
    print(solution.commonChars(["bella", "label", "roller"]))
    print(solution.commonChars(["cool", "lock", "cook"]))
    print(solution.commonChars(["a", "b", "j"]))



test()
