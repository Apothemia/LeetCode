import pytest
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        target_sum = nums_sum // 2
        candidate_sum_set = {0}
        for num in nums:
            for candidate_sum in candidate_sum_set.copy():
                candidate_sum_set.add(candidate_sum + num)
            if target_sum in candidate_sum_set:
                return True
        return False


@pytest.mark.parametrize('nums, out', [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.canPartition(nums) == out
