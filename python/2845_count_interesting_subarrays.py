import pytest
from typing import List
from collections import defaultdict, Counter


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        count[0] = 1
        interesting_subs = 0
        prefix_sum = 0
        for i in range(n):
            prefix_sum += 1 if nums[i] % modulo == k else 0
            interesting_subs += count[(prefix_sum - k + modulo) % modulo]
            count[prefix_sum % modulo] += 1
        return interesting_subs


@pytest.mark.parametrize('nums, modulo, k, out', [
    ([3, 2, 4], 2, 1, 3),
    ([3, 1, 9, 6], 3, 0, 2),
])
def test_all(nums, modulo, k, out):
    test_sol = Solution()
    assert test_sol.countInterestingSubarrays(nums, modulo, k) == out
