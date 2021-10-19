from strings.string_ops import MyString


class KMP:

    def __init__(self):
        pass

    # Iterate i in T till mismatch
    # If mismatched and part of P already be compared and matched (j >=1), then we want to check if we
    # can make some jumps in T to avoid exhaustive search

    # 0 1 2 3 4, i = 0, 1, 2, 3, 4; j = 4
    # a b a b c
    # a b a b e* f(j) = [0, 0, 1, 2, 0]

    # If brute force, checking indices for `b a b` (Note `a` has already been compared)
    # Compare 4 times, increase the index of T by one
    # a b a b c
    #   a*b a b e      bad index

    # a b a b c
    #     a b a*b e  first two matches

    # a b a b c
    #       a*b a b e    bad index

    # a b a b c
    #         a*b a b e   bad index

    # If use failure function to jump
    # Only need to compare 1 time
    # j = f(3) = 2
    # a b a b c
    #     a b a*

    # If mismatch and j>=1, check if previous compared P to see there are prefix = suffix to jump a prefix in P.
    #    (f(j) = length of longest prefix of P equals the suffix of P[1, j], max=j, note it is 1 here
    #    j = f(j - 1), then start with the jumped index (max prefix length + 1) continue check T[i] = P[j]
    # If mismatch and j = 0 (the first letter), move to the next index of T
    #    j = 0 and i + 1, start with next in the index

    # Examples: * means mismatch, - means prefix match suffix
    # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5

    # a b a c a-a*b a c c*a b a c a b
    # a b a c a-b*                       j = 0, 1, 2, 3, 4, 5. i = 0, 1, 2, 3, 4, 5 -> T[5] != P[5]
    #         a-b*                       j = f(4) = 1. i = 5  -> T[5] != P[1], check prefix = suffix to skip
    #           a b a c a*               j = f(1) = 0, 1, 2, 3, 4. i = 5, 6, 7, 8, 9 -> T[9] != P[4]
    #                   a*               j = f(3) = 0. i = 9 -> T[9] != P[0]
    #                     a b a c a b    j = 0, 1, 2, 3, 4, 5. i = 10, 11, 12, 13, 14, 15, now T[14] = P[5], end

    # a b a c a a b a c c a b a c a b
    # c*
    #   c*
    #     c*
    #       c a

    # a b a c a a b a c c a b a c a b
    # a c*
    #   a*
    #     a c c*
    #         a c*
    #           a c*
    #             a*
    #               a c c

    # a b a c a a b a c c a b a c a b
    # d*
    #   d*
    #     d*
    #       ....
    #                               d*

    def match(self, string: MyString, pattern: MyString) -> int:
        j = 0
        i = 0
        failure = self.failure_function(pattern)
        while i < string.length():
            # If match, continue index by 1
            if string.char_at(i) == pattern.char_at(j):
                if j == pattern.length() - 1:
                    # a b c d
                    #     c d
                    return i - pattern.length() + 1
                i += 1
                j += 1
            elif j > 0:
                j = failure[j - 1]
            else:
                i += 1
        return -1

    def failure_function(self, pattern: MyString) -> list:
        # b a b c
        # a b a b c

        # Brute-force way

        # b a b c
        # a*

        # b a b c
        #   a b a*

        # b a b c
        #       a*

        # Examples:
        # f(0) = 0

        # i = index in T
        # j = already matched indices

        # for each i, figure out its matched index j

        # b a b c           i = 1, `b`
        # a*                j = 0 (beginning), T[1] != P[0]. Count how many j are moved
        # f(1) = 0
        # i ++

        # b a b c           i = 2, `a`
        #   a               j = 0, T[2] = P[0], f(2) = j + 1 = 1
        # i++, j++

        # b a b c           i = 3, `b`
        #   a b             j = 1, T[3] = P[1], f(3) = j + 1 = 2
        # i++, j++

        # b a b c           i = 4, `c`
        #   a b a*          j = 2, T[4] != P[2], check if P's suffix can be jumped by any prefix. f(1) = 0
        # b a b c
        #       a*          j = 0, T[4] != P[0], f(4) = 0


        # T: b a c a b
        # P: a b a c a b

        # b a c a b         i=1, j=0, f(1) = 0
        # a*

        # b a c a b         i=2, j=0, f(2) = 1
        #   a

        # b a c a b         i=3, j=1, T[3] != P[1]
        #   a b*

        # b a c a b         i=3, j=0, T[3] != P[0], f(3) = 0
        #     a*

        # b a c a b         i=4, j=0, T[4] = P[0], f(4) = 1
        #       a

        # b a c a b         i=5, j=1, T[5] = P[1], f(5) = 2
        #       a b

        # [0, 0, 1, 0, 1, 2]

        failure = [0] * pattern.length()
        # Compare pattern with pattern itself
        i = 1
        j = 0

        while i < pattern.length():
            if pattern.char_at(i) == pattern.char_at(j):
                # j represented the matched prefix before i
                failure[i] = j + 1
                i += 1
                j += 1
            # if not matched and j > 0 meaning there are previously matched P
            # check prefix f(j - 1) for a jump
            elif j > 0:
                j = failure[j - 1]
            else:
                # if not matched and j = 0 meaning the beginning of the pattern
                # then mark f[i] = 0
                # move to next i
                failure[i] = 0
                i += 1

        return failure


string = MyString(['a', 'b', 'a', 'c', 'a', 'a', 'b', 'a', 'c', 'c', 'a', 'b', 'a', 'c', 'a', 'b'])
pattern1 = MyString(['a', 'b', 'a', 'c', 'a', 'b'])
pattern2 = MyString(['c', 'a'])
pattern3 = MyString(['a', 'c', 'c'])
pattern4 = MyString(['d'])
pattern5 = MyString(['a', 'b', 'a', 'b', 'c'])

kmp = KMP()
print(kmp.match(string, pattern1))
print(kmp.match(string, pattern2))
print(kmp.match(string, pattern3))
print(kmp.match(string, pattern4))


print(kmp.failure_function(pattern1))
print(kmp.failure_function(pattern5))


