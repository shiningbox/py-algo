from typing import List
from typing import Optional

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index_dict = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            # If encounter an seen character
            # and its last index is greater and equal than start
            # it means the current substring can not be extended anymore
            # need a new start
            # e.g., abcdc, end = c, and after start a
            # then abcdc, bcdc, cdc, can not be substrings anymore and can be skipped
            if s[end] in last_index_dict.keys() and start <= last_index_dict[s[end]]:
                start = last_index_dict[s[end]] + 1
            # if it is a new char
            # or the char's last seen position is before start
            # extend the substring
            else:
                max_len = max(max_len, end - start + 1)

            last_index_dict[s[end]] = end

        return max_len



def test():
    solution = Solution()
    # test method
    print(solution.lengthOfLongestSubstring("abcabcbb"))
 #   print(solution.lengthOfLongestSubstring("pwwkew"))
#    print(solution.lengthOfLongestSubstring(""))
#    print(solution.lengthOfLongestSubstring(" "))
 #   print(solution.lengthOfLongestSubstring("a"))


test()
