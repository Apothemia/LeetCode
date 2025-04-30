import pytest
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for num in nums if not len(str(num)) % 2])


@pytest.mark.parametrize('nums, out', [
    ([12, 345, 2, 6, 7896], 2),
    ([555, 901, 482, 1771], 1),
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.findNumbers(nums) == out
