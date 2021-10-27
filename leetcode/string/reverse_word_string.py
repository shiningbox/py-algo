from typing import List
from typing import Optional

# Given a string s, reverse the order of characters in each
# word within a sentence while still preserving whitespace and initial word order.
class Solution:

    def reverse(self, sub_string):
        s_array = [c for c in sub_string]
        l = 0
        e = len(s_array) - 1
        while l < e:
            s_array[l], s_array[e] = s_array[e], s_array[l]
            l += 1
            e -= 1
        return "".join([c for c in s_array])

    def reverseWords(self, s: str) -> str:
        start = end = 0
        results = ""
        while start < len(s) and end < len(s):
            # Move end till the next
            while end < len(s) and s[end] != " ":
                end += 1
            if end <= len(s):
                # do not include the last index
                if end < len(s):
                    results += self.reverse(s[start:end]) + " "
                else:
                    results += self.reverse(s[start:end])
            end += 1
            start = end
        return results

def test():
    solution = Solution()
    # test method
    print(solution.reverseWords("Let's take LeetCode contest"))


test()
