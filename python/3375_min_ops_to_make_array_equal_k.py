import pytest
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        if min_num < k:
            return -1
        num_set = set(nums)
        if min_num == k:
            return len(num_set) - 1
        return len(num_set)

        # nums = list(sorted(set(nums)))
        # if nums[0] == k:
        #     return len(nums) - 1
        # if nums[0] < k:
        #     return -1
        # return len(nums)


# if __name__ == '__main__':
#     s = Solution()
#     print(s.minOperations([5, 2, 5, 4, 5], 2))
#
@pytest.mark.parametrize('nums, k, out', [
    ([5, 2, 5, 4, 5], 2, 2),
    ([2, 1, 2], 2, -1),
    ([9, 7, 5, 3], 1, 4),
])
def test_all(nums, k, out):
    test_sol = Solution()
    assert test_sol.minOperations(nums, k) == out
