from typing import List
from typing import Optional


class Solution:
    """ d[i] = True means s[:i+1] can all be assembled from word dict
            d[j] is True at the beginning of the word j = i - len(word)
                                    AND
            If there is a word in the dictionary that ends at ith index of s
            w == s[j + 1:i + 1]

        Example:

        s = "leetcode"
        words = ["leet", "code"]

        d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

        d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode"
            AND
        d[3] is True


        """
    def wordBreak(self, s, words):
        d = [False] * len(s)
        for i in range(len(s)):
            # For each word, check if any word can make d[i] to be true
            for w in words:
                begin_idx = i - len(w)
                if begin_idx < -1:
                    continue
                if w == s[begin_idx + 1:i + 1] and (d[begin_idx] or begin_idx == -1):
                    d[i] = True
                    break
        return d[-1]


def test():
    solution = Solution()
    # test method
    #print(solution.wordBreak("applepenapple", ["apple", "pen"]))
    #print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    #print(solution.wordBreak("abcd", ["a","abc","b","cd"]))
    print(solution.wordBreak("aaaaaaa", ["aaaa","aa"]))

test()
