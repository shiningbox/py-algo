from typing import List
from typing import Optional

class Solution:
    # The student was absent ('A') for strictly fewer than 2 days total.
    # The student was never late ('L') for 3 or more consecutive days.
    def checkRecord(self, s: str) -> bool:
        i = 0
        count = {}
        count['A'] = 0
        is_late = False
        l_count = 0
        while i < len(s):
            if s[i] == 'A':
                if s[i] not in count:
                    count[s[i]] = 1
                else:
                    count[s[i]] += 1
            else:
                if not is_late:
                    # Check if it is late
                    if s[i] == 'L':
                        l_count = 1
                        j = i + 1
                        while j < len(s) and s[j] == 'L':
                            l_count += 1
                            j += 1
                        if l_count >= 3:
                            is_late = True
                            break
            i += 1
        return count['A'] < 2 and not is_late


def test():
    solution = Solution()
    # test method
    print(solution.checkRecord("PPALLP"))
    print(solution.checkRecord("PPALLL"))
    print(solution.checkRecord("A"))
    print(solution.checkRecord("LLL"))
    print(solution.checkRecord("LL"))
    print(solution.checkRecord("ALLAA"))


test()
