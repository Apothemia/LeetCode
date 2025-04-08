import pytest
from typing import List
import math


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct_nums = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in distinct_nums:
                return math.ceil((i + 1) / 3)
            distinct_nums.add(nums[i])
        return 0


@pytest.mark.parametrize('nums, out', [
    ([1, 2, 3, 4, 2, 3, 3, 5, 7], 2),
    ([4, 5, 6, 4, 4], 2),
    ([6, 7, 8, 9], 0),
    ([2, 7, 15, 1, 15], 1),
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.minimumOperations(nums) == out
