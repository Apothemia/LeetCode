import pytest
import bisect
from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        mpp = {num: idx for idx, num in enumerate(nums1)}
        good_triplets = 0
        stack = []
        for x in nums2:
            idx = mpp[x]
            left = bisect.bisect_left(stack, idx)
            right = n - 1 - idx - len(stack) + left
            good_triplets += left * right
            bisect.insort(stack, idx)
        return good_triplets


@pytest.mark.parametrize('nums1, nums2, out', [
    ([2, 0, 1, 3], [0, 1, 2, 3], 1),
    ([4, 0, 1, 3, 2], [4, 1, 0, 2, 3], 4),
])
def test_all(nums1, nums2, out):
    test_sol = Solution()
    assert test_sol.goodTriplets(nums1, nums2) == out
