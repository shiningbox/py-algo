from typing import List
from typing import Optional

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for n in nums:
            if n not in freq_dict:
                freq_dict[n] = 1
            else:
                freq_dict[n] += 1
        bucket = [None] * (len(nums) + 1)
        # Large frequence will be assigned towards the end of the bucket
        for key, freq in freq_dict.items():
            if not bucket[freq]:
                bucket[freq] = [key]
            else:
                bucket[freq].append(key)
        res = []
        print(bucket)
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] and len(res) < k:
                res.extend(bucket[i])
        return res


def test():
    solution = Solution()
    # test method
    #print(solution.topKFrequent([1,1,1,2,2,3], 2))
    #print(solution.topKFrequent([1], 1))
    print(solution.topKFrequent([4,1,-1,2,-1,2,3], 2))


test()
