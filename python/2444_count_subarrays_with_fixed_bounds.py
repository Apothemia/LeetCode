import pytest
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        last_invalid_idx, min_idx, max_idx = -1, -1, -1
        subarray_count = 0
        for i in range(n):
            if nums[i] == minK:
                min_idx = i
            if nums[i] == maxK:
                max_idx = i
            if nums[i] < minK or nums[i] > maxK:
                last_invalid_idx = i
            subarray_count += max(0, min(min_idx, max_idx) - last_invalid_idx)
        return subarray_count


@pytest.mark.parametrize('nums, minK, maxK, out', [
    ([1, 3, 5, 2, 7, 5], 1, 5, 2),
    ([1, 1, 1, 1], 1, 1, 10),
])
def test_all(nums, minK, maxK, out):
    test_sol = Solution()
    assert test_sol.countSubarrays(nums, minK, maxK) == out
