from typing import List
from collections import Counter
import pytest


class Solution:
    def minimumIndexBinarySearch(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1

        initial_counts = Counter(nums)
        nums_dom, nums_dom_count = initial_counts.most_common(1)[0]

        if nums_dom_count == len(nums):
            return 0

        start, end = 0, len(nums) - 1
        while start < end:
            first_split_valid = second_split_valid = False
            mid = (start + end) // 2

            first_split_dom, first_split_count = Counter(nums[:mid + 1]).most_common(1)[0]
            if first_split_dom == nums_dom and first_split_count * 2 > len(nums[:mid + 1]):
                first_split_valid = True

            second_split_dom, second_split_count = Counter(nums[mid + 1:]).most_common(1)[0]
            if second_split_dom == nums_dom and second_split_count * 2 > len(nums[mid + 1:]):
                second_split_valid = True

            if first_split_valid and second_split_valid:
                return mid
            if not first_split_valid and not second_split_valid:
                return -1

            if not first_split_valid:
                start = mid + 1
            elif not second_split_valid:
                end = mid
        return -1

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return -1

        dom_num, total_dom_count = Counter(nums).most_common(1)[0]
        if total_dom_count == n:
            return 0

        curr_dom_count = 0
        for i in range(n):
            if nums[i] == dom_num:
                curr_dom_count += 1
            if curr_dom_count * 2 > i + 1 and (total_dom_count - curr_dom_count) * 2 > n - (i + 1):
                return i
        return -1


@pytest.mark.parametrize('nums, out', [
    ([3, 3, 3, 3, 7, 2, 2], -1),
    ([2, 1, 3, 1, 1, 1, 7, 1, 2, 1], 4),
    ([1, 2, 1, 1], 0),
    ([1], -1),
    ([1, 1, 1], 0),
    ([1, 2, 2, 2], 2),
    ([1, 2, 1], -1),
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.minimumIndex(nums) == out
