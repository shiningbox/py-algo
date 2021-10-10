from typing import List
from typing import Optional

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_dict = {}
        m_dict = {}

        for char in ransomNote:
            if char not in r_dict.keys():
                r_dict[char] = 1
            else:
                count = r_dict[char]
                r_dict[char] = count + 1

        for char in magazine:
            if char not in m_dict.keys():
                m_dict[char] = 1
            else:
                count = m_dict[char]
                m_dict[char] = count + 1

        for key in r_dict.keys():
            if key in m_dict.keys() and m_dict[key] >= r_dict[key]:
                continue
            else:
                return False

        return True

def test():
    solution = Solution()
    # test method
    print(solution.canConstruct("a", "b"))
    print(solution.canConstruct("aa", "ab"))
    print(solution.canConstruct("aa", "aab"))



test()
