
from typing import List
from typing import Optional

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i
        order_dict['N'] = -1
        max_length = max([len(word) for word in words])
        for i in range(0, max_length):
            j = 1

            all_sorted = True
            pre_char = 'N'

            while j < len(words):
                current_char = 'N'
                if i < len(words[j-1]):
                    pre_char = words[j-1][i]

                if i < len(words[j]):
                    current_char = words[j][i]

                if order_dict[pre_char] > order_dict[current_char]:
                    return False
                elif order_dict[pre_char] < order_dict[current_char]:
                    pass
                else:
                    all_sorted = False

                pre_char = current_char
                j += 1

            if all_sorted:
                return True

        return True

def test():
    solution = Solution()
    # test method
    print(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
    print(solution.isAlienSorted(["hello", "hello"], "abcdefghijklmnopqrstuvwxyz"))
    print(solution.isAlienSorted(["aa", "aa"], "abcdefghijklmnopqrstuvwxyz"))
    print(solution.isAlienSorted(["apple","apple","app"], "abcdefghijklmnopqrstuvwxyz"))


test()
