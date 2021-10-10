from typing import List
from typing import Optional

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        char_list = [char for char in s]
        h = len(char_list) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l < h:

            if char_list[l] not in vowels:
                l += 1

            if char_list[h] not in vowels:
                h -= 1


            if char_list[l] in vowels and char_list[h] in vowels:
                # swap l and h
                temp = char_list[l]
                char_list[l] = char_list[h]
                char_list[h] = temp
                l += 1
                h -= 1

        return "".join(char_list)

def test():
    solution = Solution()
    # test method
    print(solution.reverseVowels("hello"))
    print(solution.reverseVowels("leetcode"))
    print(solution.reverseVowels("a"))


test()
