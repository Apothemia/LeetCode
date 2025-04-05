import pytest
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs_sum(subset_sum, i):
            if i == len(nums):
                return subset_sum
            return dfs_sum(subset_sum ^ nums[i], i + 1) + dfs_sum(subset_sum, i + 1)

        return dfs_sum(0, 0)


@pytest.mark.parametrize('nums, out', [
    ([1, 3], 6),
    ([5, 1, 6], 28),
    ([3, 4, 5, 6, 7, 8], 480)
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.subsetXORSum(nums) == out
