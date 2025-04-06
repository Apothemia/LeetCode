import pytest
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]
        largest_sub_idx = -1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    subset = dp[j] + [nums[i]]
                    if len(subset) > len(dp[i]):
                        dp[i] = subset
            if len(dp[i]) > len(dp[largest_sub_idx]):
                largest_sub_idx = i
        return dp[largest_sub_idx]


@pytest.mark.parametrize('nums, out', [
    ([1, 2, 3], [1, 2]),
    ([1, 2, 4, 8], [1, 2, 4, 8]),
    ([2, 3, 6, 18], [3, 6, 18]),
    ([3, 4, 16, 8], [4, 8, 16])
])
def test_all(nums, out):
    test_sol = Solution()
    assert set(test_sol.largestDivisibleSubset(nums)) == set(out)
