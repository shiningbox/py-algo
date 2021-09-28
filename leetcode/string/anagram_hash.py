from typing import List
from typing import Optional

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        dict_a = {}
        dict_b = {}
        for char in s:
            if char not in dict_a:
                dict_a[char] = 1
            else:
                dict_a[char] += 1
        for char in t:
            if char not in dict_b:
                dict_b[char] = 1
            else:
                dict_b[char] += 1

        if len(dict_a.keys()) != len(dict_b.keys()):
            return False

        for key in dict_a.keys():
            if key not in dict_b.keys():
                return False

            if dict_a[key] != dict_b[key]:
                return False

        return True

def test():
    solution = Solution()
    # test method
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("cat", "rat"))
    print(solution.isAnagram("a", "ab"))

test()
