from typing import List
from typing import Optional

class Solution:

    def create_dicts(self, s):
        dict_a = {}
        # Add char frequency to dict
        for char in s:
            if char not in dict_a:
                dict_a[char] = 1
            else:
                dict_a[char] += 1
        return dict_a

    def isAnagram(self, dicts, s: str, t: str) -> bool:

        dict_a = dicts[s]
        dict_b = dicts[t]

        if len(dict_a.keys()) != len(dict_b.keys()):
            return False

        for key in dict_a.keys():
            if key not in dict_b.keys():
                return False

            # If char frequencies are different
            if dict_a[key] != dict_b[key]:
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())

    def groupAnagrams_on2(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return [[""]]
        dicts = {}
        for s in strs:
            dicts[s] = self.create_dicts(s)

        groups = []

        for word in strs:
            new_group = True
            for group in groups:
                if len(group) > 0:
                    if self.isAnagram(dicts, word, group[0]):
                        group += [word]
                        new_group = False
                        break

            if new_group:
                groups.append([word])

        return groups


def test():
    solution = Solution()
    # test method
    print(solution.groupAnagrams_on2(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams_on2([]))


test()
