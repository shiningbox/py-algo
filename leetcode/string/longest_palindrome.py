from typing import List
from typing import Optional

class Solution:

    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        matrix = [[0 for i in range(lens)] for j in range(lens)]
        max_indices = (0, 0)

        for end in range(lens):
            for start in range(0, end + 1):
                if start == end:
                    matrix[end][start] = 1
                elif end - start == 1:
                    if s[start] == s[end]:
                        matrix[end][start] = 1
                        if end - start > max_indices[1] - max_indices[0]:
                            max_indices = (start, end)
                else:
                    # check if from end - 1 to start + 1 is palindrome
                    # if yes, then check if s[start] == s[end]
                    if matrix[end - 1][start + 1] == 1 and s[start] == s[end]:
                        matrix[end][start] = 1
                        if end - start > max_indices[1] - max_indices[0]:
                            max_indices = (start, end)

        return s[max_indices[0]: max_indices[1] + 1]


    def longestPalindrome_on2(self, s: str) -> str:
        lens = len(s)
        matrix = [[0 for i in range(lens)] for j in range(lens)]
        max_indices = (0, 0)

        for end in range(lens):
            for start in range(0, end + 1):
                if start == end:
                    matrix[end][start] = 1
                elif end - start == 1:
                    if s[start] == s[end]:
                        matrix[end][start] = 1
                        if end - start > max_indices[1] - max_indices[0]:
                            max_indices = (start, end)
                else:
                    # check if from end - 1 to start + 1 is palindrome
                    # if yes, then check if s[start] == s[end]
                    if matrix[end - 1][start + 1] == 1 and s[start] == s[end]:
                        matrix[end][start] = 1
                        if end - start > max_indices[1] - max_indices[0]:
                            max_indices = (start, end)

        return s[max_indices[0]: max_indices[1] + 1]


def test():
    solution = Solution()
    # test method
    print(solution.longestPalindrome("abb"))
    print(solution.longestPalindrome("ccc"))
    print(solution.longestPalindrome("cbbd"))
    print(solution.longestPalindrome("babad"))
    print(solution.longestPalindrome("ababd"))
    print(solution.longestPalindrome("a"))
    print(solution.longestPalindrome("c"))
    print(solution.longestPalindrome("rgszobovkyonbtpsjnygxkugokdascyhwvqiawupiesrqewwyxwzqfalcgtnyppflgghrkwvwtaugkllyqoonzobflqjkcmhlstbmqungfzvbkucdrvciifriaebpicmuavesdnucgmhdmzkpwocerostwzipukprmpcltrkvafgqavfhhmojwypttnymjgluohwzhjlmxluvosyfcnajuvphlrmzdmmmyarpnhmypgygshuegfnnlktotiqpmjtuaigxechjtwwvceqrfmtzwevryyhivbcsgnldfiaedbummzzqfasmpveyzasgleiuqltwauvdaheesaaroytlhfdyjsjwgfpgllmwajkujooahsspfirjeyimoacfzcojqgpiqtplkondgfiqqxwakkwvsrumkalvdtokrityxwxmsmprraotxheqgthpucugjlhrllakkbfmmfbkkallrhljgucuphtgqehxtoarrpmsmxwxytirkotdvlakmursvwkkawxqqifgdnoklptqipgqjoczfcaomiyejrifpsshaoojukjawmllgpfgwjsjydfhltyoraaseehadvuawtlquielgsazyevpmsafqzzmmubdeaifdlngscbvihyyrvewztmfrqecvwwtjhcexgiautjmpqitotklnnfgeuhsgygpymhnpraymmmdzmrlhpvujancfysovulxmljhzwhoulgjmynttpywjomhhfvaqgfavkrtlcpmrpkupizwtsorecowpkzmdhmgcundsevaumcipbeairfiicvrdcukbvzfgnuqmbtslhmckjqlfboznooqyllkguatwvwkrhgglfppyntgclafqzwxywweqrseipuwaiqvwhycsadkogukxgynjsptbnoykvobozsgr"))


test()
