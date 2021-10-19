from typing import List
from typing import Optional

class Solution:

    #O(n2)
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub_lens = []
        for i in range(1, len(s) // 2 + 1):
            if s[0] == s[i]:
                sub_lens.append(i)

        if not sub_lens:
            return False
        print(sub_lens)
        results = []
        for sub_len in sub_lens:
            result = True
            num_sub = len(s) // sub_len
            if num_sub < 2 or len(s) % sub_len != 0:
                result = False
                results.append(result)
                continue
            else:
                for i in range(sub_len):
                    for j in range(1, num_sub, 1):
                        if s[i] != s[j * sub_len + i]:
                            result = False
                            results.append(result)

            if result:
                return True

        return False

def test():
    solution = Solution()
    # test method
    print(solution.repeatedSubstringPattern("abcdef"))
    print(solution.repeatedSubstringPattern("aaaa"))
    print(solution.repeatedSubstringPattern("abab"))
    print(solution.repeatedSubstringPattern("abcabcabc"))
    print(solution.repeatedSubstringPattern("abcbcabc"))
    print(solution.repeatedSubstringPattern("a"))
    print(solution.repeatedSubstringPattern("abaababaab"))
    print(solution.repeatedSubstringPattern("ababababab"))
    print(solution.repeatedSubstringPattern("abac"))
    print(solution.repeatedSubstringPattern("babbabbabbabbab"))


test()
