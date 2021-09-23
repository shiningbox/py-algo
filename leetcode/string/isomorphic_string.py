from typing import List
from typing import Optional

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        new_str = []
        for i in range(len(s)):
            # Create a one-to-one mapping
            # i.e., a character can not be mapped to different characters
            if s[i] not in char_dict.keys() and \
                    t[i] not in char_dict.values():
                char_dict[s[i]] = t[i]
            # if, character in t is already mapped
            elif s[i] not in char_dict.keys() and t[i] in char_dict.values():
                return False
            # If there is a mapping created
            if s[i] in char_dict:
                new_str.append(char_dict[s[i]])

        return "".join(new_str) == t

def test():
    solution = Solution()
    # test method
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("badc", "baba"))
    print(solution.isIsomorphic("egcd", "adfd"))
    print(solution.isIsomorphic("a", "a"))


test()
