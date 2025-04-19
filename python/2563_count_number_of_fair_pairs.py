import pytest
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count_pairs_up_to_target(target):
            fair_pairs = 0
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                else:
                    fair_pairs += right - left
                    left += 1
            return fair_pairs

        nums.sort()
        return count_pairs_up_to_target(upper) - count_pairs_up_to_target(lower - 1)


@pytest.mark.parametrize('nums, lower, upper, out', [
    ([0, 1, 7, 4, 4, 5], 3, 6, 6),
    ([1, 7, 9, 2, 5], 11, 11, 1),
    ([-5, -7, -5, -7, -5], -12, -12, 6)
])
def test_all(nums, lower, upper, out):
    test_sol = Solution()
    assert test_sol.countFairPairs(nums, lower, upper) == out
