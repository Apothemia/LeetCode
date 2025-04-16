import pytest
from collections import Counter
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1
        counter = Counter()
        good_arrays = 0
        for left in range(n):
            print(counter)
            while same < k and right + 1 < n:
                right += 1
                same += counter[nums[right]]
                counter[nums[right]] += 1
            if same >= k:
                good_arrays += n - right
            counter[nums[left]] -= 1
            same -= counter[nums[left]]
        return good_arrays


@pytest.mark.parametrize('nums, k, out', [
    ([1, 1, 1, 1, 1], 10, 1),
    ([3, 1, 4, 3, 2, 2, 4], 2, 4),
    ([1, 2, 3, 4, 1, 3, 5, 4, 1, 1, 1], 10, 1),
    ([3, 1, 9, 8, 7, 4, 3, 2, 4, 5, 6, 9, 8, 2, 4], 2, 24),
    ([1], 20, 0),
    ([3, 3, 3, 3, 3, 3, 1], 12, 2),
    ([1, 2, 2, 3, 1, 1, 1], 3, 6)
])
def test_all(nums, k, out):
    test_sol = Solution()
    assert test_sol.countGood(nums, k) == out
