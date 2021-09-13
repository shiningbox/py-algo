from typing import List

class Solution:

    def initial_dict(self):
        ro_dict = {}
        ro_dict['I'] = 1
        ro_dict['IV'] = 4
        ro_dict['V'] = 5
        ro_dict['IX'] = 9
        ro_dict['X'] = 10
        ro_dict['XL'] = 40
        ro_dict['XL'] = 40
        ro_dict['L'] = 50
        ro_dict['XC'] = 90
        ro_dict['C'] = 100
        ro_dict['CD'] = 400
        ro_dict['D'] = 500
        ro_dict['CM'] = 900
        ro_dict['M'] = 1000
        return ro_dict

    def romanToInt(self, s: str) -> int:

        "I 1"
        "V 5"
        "X 10"
        "L 50"
        "C 100"
        "D 500"
        "M 1000"
        ro_dict = self.initial_dict()
        # IV, IX
        # XL, XC
        # CD, CM
        i = 0
        l = len(s)
        value = 0
        while i <= l - 1:
            num = ro_dict[s[i]]
            # If finds I, and next element is X or V
            if i < l - 1:
                key = s[i] + s[i + 1]
                if key in ro_dict:
                    num = ro_dict[key]
                    i += 1
            value += num
            i += 1
        return value


def test():
    solution = Solution()
    # test method
    print(solution.romanToInt("II"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
    print(solution.romanToInt("DCXXI"))


test()
