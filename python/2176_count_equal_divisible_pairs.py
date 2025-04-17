import pytest
from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        index_list = defaultdict(list)
        for i in range(n):
            index_list[nums[i]].append(i)
        pair_count = 0
        for equal_pairs in index_list.values():
            pair_len = len(equal_pairs)
            if pair_len < 2:
                continue
            for i in range(pair_len - 1):
                for j in range(i + 1, pair_len):
                    if (equal_pairs[i] * equal_pairs[j]) % k == 0:
                        pair_count += 1
        return pair_count


@pytest.mark.parametrize('nums, k, out', [
    ([3, 1, 2, 2, 2, 1, 3], 2, 4),
    ([1, 2, 3, 4], 1, 0)
])
def test_all(nums, k, out):
    test_sol = Solution()
    assert test_sol.countPairs(nums, k) == out
