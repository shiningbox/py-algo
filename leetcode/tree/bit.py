from typing import List
from typing import Optional

"""Binary Indexed Tree is represented as an array.
Each node of the Binary Indexed Tree stores the sum of n elements (power of 2) of the input array.
depending on the updating process"""


"""Given any integer, which has a binary format, i.e., a sum of powers of 2"""

"""e.g., 9: 1001 = 8 1000 + 1 0001, i.e., the 1 bits in the number"""

"""
For getting sum, the child node BITree[x] of the node BITree[y] stores the 
sum of the elements between y(inclusive) and x(exclusive): arr[y,…,x). 
- The parent of index i in the getting tree is:  
i -= (i & -i)
e.g., 12 1100 - 0100 = 8 1000, thus 8 is the parent of 12
"""

"""
For updating BITree[x], we need to add the value to all its ancestors. 

It stores the sum from x to its smallest child, e.g., 

e.g., suppose we have 8 numbers
             8 
         4    6   7
        2  3   5
      1
      
BITree[1] stores sum from 1 to 1 arr[0:1]
BITree[2] stores sum from 1 to 2 arr[0:2]
BITree[4] stores sum from 1 to 4 arr[0:4]
BITree[8] stores sum from 1 to 8 (arr[0:8])
BITree[6] stores sum from 5 to 6 (arr[4:6])


For updating BITree[x], we need to add the value to all its ancestors as well because it is within its ancesters' sum range
e.g., update BITree[1] will need to update BITree[2], BITree[4], BITree[8]

How to determine parent and construct the BITree from 1 to n?

- The parent of index i in the updating tree is: 
i += (i & -i)
e.g., 4 0100 & -4 1100 = 4 0010
Thus 4 0010 + 4 0010 = 8 0100 thus 8 is the parent of 4

"""


def getsum(bit, i):
    s = 0  # initialize result

    # index in BITree[] is 1 more than the index in arr[]
    i = i + 1

    # Traverse ancestors of BITree[index]
    while i > 0:
        # Add current element of BITree to sum
        s += bit[i]

        i -= i & (-i)

    return s


# Updates a node in Binary Index Tree (BITree) at given index
# in BITree. The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(bit, n, i, v):
    # index in BITree[] is 1 more than the index in arr[]
    i += 1

    # Traverse all ancestors and add 'val'
    while i <= n:
        # Add 'val' to current node of BI Tree
        bit[i] += v

        # Update index to that of parent in update View
        i += i & (-i)


# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
    # Create and initialize BITree[] as 0
    bit = [0] * (n + 1)

    # Store the actual values in BITree[] using update()
    for i in range(n):
        updatebit(bit, n, i, arr[i])

    # Uncomment below lines to see contents of BITree[]
    # for i in range(1,n+1):
    #     print BITTree[i],
    return bit


# Driver code to test above methods
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITTree = construct(freq, len(freq))

print("Sum of elements in arr[0..5] is " + str(getsum(BITTree, 5)))

freq[3] += 6
updatebit(BITTree, len(freq), 3, 6)
print("Sum of elements in arr[0..5]" +
      " after update is " + str(getsum(BITTree, 5)))
