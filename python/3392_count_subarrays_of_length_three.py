import pytest
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i] % 2 == 0 and 2 * (nums[i - 1] + nums[i + 1]) == nums[i]:
                count += 1
        return count


@pytest.mark.parametrize('nums, out', [
    ([1, 2, 1, 4, 1], 1),
    ([1, 1, 1], 0),
    ([0, 0, 0, 0], 2)
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.countSubarrays(nums) == out
