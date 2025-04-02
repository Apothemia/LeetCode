import pytest
from heapq import heapify, heappop
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            solve, skip = points, 0
            if i + 1 < n:
                skip = dp[i + 1]
                if i + 1 + brainpower < n:
                    solve += dp[i + 1 + brainpower]
            dp[i] = max(solve, skip)
        return dp[0]


@pytest.mark.parametrize('questions, out', [
    ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
    ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
])
def test_all(questions, out):
    test_sol = Solution()
    assert test_sol.mostPoints(questions) == out
