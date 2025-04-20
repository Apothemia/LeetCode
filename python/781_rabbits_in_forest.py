import pytest
from typing import List
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(-(-v // (k + 1)) * (k + 1) for k, v in Counter(answers).items())


@pytest.mark.parametrize('answers, out', [
    ([1, 1, 2], 5),
    ([10, 10, 10], 11),
    ([1, 0, 1, 0, 0], 5),
    ([0, 0, 1, 1, 1], 6)
])
def test_all(answers, out):
    test_sol = Solution()
    assert test_sol.numRabbits(answers) == out
