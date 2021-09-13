from typing import List

class Solution:

    def isPalindrome(self, x: int) -> bool:

        is_palindrome = True

        if x < 0:
            return False

        digits = []
        value = x
        while value != 0:
            digits.append(value % 10)
            value = int(value / 10)

        h = 0
        t = len(digits) - 1

        while t > h:
            if digits[h] != digits[t]:
                is_palindrome = False
                break
            t -= 1
            h += 1
        return is_palindrome

def test():
    solution = Solution()
    # test method
    print(solution.isPalindrome(10))
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(1221))
    print(solution.isPalindrome(23132))



test()
