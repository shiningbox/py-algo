def update_dict(c_dict, c, op):
    if c in c_dict:
        if op == 'add':
            c_dict[c] += 1
        elif op == 'del':
            c_dict[c] -= 1
            if c_dict[c] == 0:
                del c_dict[c]
    else:
        if op == 'add':
            c_dict[c] = 1


def longest_substring_with_k_distinct(str1, k):
    start, end = 0, 0
    c_dict = {}
    res = 0
    while end < len(str1):
        # If the current unique character in the dict is less than k,
        # add a new character to the dict
        while end < len(str1) - 1 and len(c_dict) <= k:
            update_dict(c_dict, str1[end], 'add')
            end += 1
            if end == len(str1) - 1:
                break

        print(c_dict)

        # If the current unique character in the dict is larger than k (current sub-array),
        # then try to shrink the window (start += 1)
        # and include later character to see if the max length can be increased
        while start <= end and len(c_dict) > k:
            update_dict(c_dict, str1[start], 'del')
            start += 1

        print(end, start)
        res = max(res, end - start + 1)

    return res


def main():
    # print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    # print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
