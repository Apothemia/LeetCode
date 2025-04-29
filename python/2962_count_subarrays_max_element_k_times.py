import pytest
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, max_element = len(nums), max(nums)
        subarray_count = 0
        right, max_element_count = 0, 0
        for left in range(n):
            while right < n and max_element_count < k:
                if nums[right] == max_element:
                    max_element_count += 1
                right += 1
            if max_element_count == k:
                subarray_count += n - right + 1
            if nums[left] == max_element:
                max_element_count -= 1
        return subarray_count


@pytest.mark.parametrize('nums, k, out', [
    ([1, 3, 2, 3, 3], 2, 6),
    ([1, 4, 2, 1], 3, 0),
])
def test_all(nums, k, out):
    test_sol = Solution()
    assert test_sol.countSubarrays(nums, k) == out
