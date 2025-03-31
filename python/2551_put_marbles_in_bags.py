import pytest
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or len(weights) == k:
            return 0
        weights = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        weights.sort()
        return sum(weights[-k + 1:]) - sum(weights[:k - 1])


@pytest.mark.parametrize('weights, k, out', [
    ([1, 3, 5, 1], 2, 4),
    ([1, 9, 5, 3], 1, 0),
    ([1, 3], 2, 0),
    ([1, 4, 5], 3, 0)
])
def test_all(weights, k, out):
    test_sol = Solution()
    assert test_sol.putMarbles(weights, k) == out
