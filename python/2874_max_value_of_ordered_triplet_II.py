import pytest
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = max(nums[i - 1], left[i - 1])
            right[n - i - 1] = max(nums[n - i], right[n - i])
        max_value = 0
        for i in range(1, n - 1):
            max_value = max((left[i] - nums[i]) * right[i], max_value)
        return max_value


@pytest.mark.parametrize('nums, out', [
    ([12, 6, 1, 2, 7], 77),
    ([1, 10, 3, 4, 19], 133),
    ([1, 2, 3], 0)
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.maximumTripletValue(nums) == out
