from typing import List
from typing import Optional

class Solution:

    def split_str(self, string) -> []:
        words = []
        word = ""
        for i in range(len(string)):
            if string[i] != " ":
                word += string[i]
            else:
                words.append(word)
                word = ""
        words.append(word)
        return words

    def wordPattern(self, pattern: str, s: str) -> bool:

        str_dict = {}
        words = self.split_str(s)
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            # Trying to create new mapping
            if pattern[i] not in str_dict.keys():
                # If its mapped value already mapped with another key
                # return False
                if words[i] in str_dict.values():
                    return False
                str_dict[pattern[i]] = words[i]
            else:
                if str_dict[pattern[i]] != words[i]:
                    return False
        return True

def test():
    solution = Solution()
    # test method

    print(solution.wordPattern("abba", "dog cat cat dog"))
    print(solution.wordPattern("abba", "dog cat cat fish"))
    print(solution.wordPattern("aaaa", "dog cat cat dog"))
    print(solution.wordPattern("aaaa", "dog dog dog dog"))
    print(solution.wordPattern("abba", "dog dog dog dog"))


test()
