from typing import List
from typing import Optional


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_dict = {}

        change_dict[5] = 0
        change_dict[10] = 0
        change_dict[20] = 0

        for bill in bills:
            # Accept change
            if bill < 20:
                # Add bill to cashier
                change_dict[bill] += 1

                if bill == 10:
                    if change_dict[5] > 0:
                        # Give 5 dollars change
                        change_dict[5] -= 1
                    else:
                        return False
            else:
                # If has 10 bills
                if change_dict[10] > 0:
                    if change_dict[5] > 0:
                        change_dict[10] -= 1
                        change_dict[5] -= 1
                    else:
                        return False
                else:
                    if change_dict[5] >= 3:
                        change_dict[5] -= 3
                    else:
                        return False

        return True

def test():
    solution = Solution()
    # test method
    #print(solution.lemonadeChange([5,5,5,10,20]))
    print(solution.lemonadeChange([5,5,10,10,20]))
    print(solution.lemonadeChange([5,5,5,5,10,5,10,10,10,20]))


test()
