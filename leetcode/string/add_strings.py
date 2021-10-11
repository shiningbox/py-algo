from typing import List
from typing import Optional

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1_list = []
        nums2_list = []
        results = []
        for i in range(len(num1) - 1, -1, -1):
            nums1_list.append(ord(num1[i]) - ord('0'))

        for j in range(len(num2) - 1, -1, -1):
            nums2_list.append(ord(num2[j]) - ord('0'))
        op_nums = []
        i = 0
        carry = 0
        while i < len(nums2_list) and i < len(nums1_list):
            add = nums2_list[i] + nums1_list[i] + carry
            if add >= 10:
                results.append(str(add - 10))
                carry = 1
            else:
                results.append(str(add))
                carry = 0
            i += 1


        # if nums2 has remaining
        if len(nums2_list) - i > 0:
            op_nums = nums2_list[len(nums1_list): len(nums2_list)]
        # if nums1 has remainings
        else:
            op_nums = nums1_list[len(nums2_list): len(nums1_list)]

        del nums1_list
        del nums2_list

        for num in op_nums:
            add = num + carry
            if add >= 10:
                results.append(str(add - 10))
                carry = 1
            else:
                results.append(str(add))
                carry = 0

        if carry == 1:
            results.append("1")

        i = 0
        j = len(results) - 1

        while i < j:
            temp = results[i]
            results[i] = results[j]
            results[j] = temp
            i += 1
            j -= 1

        return "".join(results)

def test():
    solution = Solution()
    # test method
    print(solution.addStrings("11", "123"))
    print(solution.addStrings("456", "77"))
    print(solution.addStrings("12345678234", "123"))
    print(solution.addStrings("0", "0"))
    print(solution.addStrings("1", "9"))
    print(solution.addStrings("9", "99"))


test()
