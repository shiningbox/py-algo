from typing import List

class Solution:

    def extract_chars(self, s: str):
        res = []
        # A - Z, 65 to 90
        # a - z, 97 to 122
        # 0 - 9, 48 to 57
        for i in range(len(s)):
            ascii_val = ord(s[i])
            if 65 <= ascii_val <= 90:
                res.append(chr(ascii_val + 32))
            if 97 <= ascii_val <= 122 or 48 <= ascii_val <= 57:
                res.append(s[i])
        return res

    def isPalindrome(self, s: str) -> bool:
        chars = self.extract_chars(s)
        i = 0
        j = len(chars) - 1
        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1
        return True

def test():
    solution = Solution()
    # test method
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome("raar"))
    print(solution.isPalindrome("a"))
    print(solution.isPalindrome("0P"))



test()
