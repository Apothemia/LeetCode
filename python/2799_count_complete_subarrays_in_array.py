import pytest
from typing import List
from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, dist_max = len(nums), len(set(nums))
        dist_count_dict = defaultdict(int)
        complete_count = 0
        right = 0
        for left in range(n):
            while right < n and len(dist_count_dict) < dist_max:
                dist_count_dict[nums[right]] += 1
                right += 1
            if len(dist_count_dict) == dist_max:
                complete_count += n - right + 1
            del_num = nums[left]
            dist_count_dict[del_num] -= 1
            if dist_count_dict[del_num] == 0:
                del dist_count_dict[del_num]
        return complete_count


# if __name__ == '__main__':
#     s = Solution()
#     print(s.countCompleteSubarrays([1, 3, 1, 2, 2]))
@pytest.mark.parametrize('nums, out', [
    ([1, 3, 1, 2, 2], 4),
    ([5, 5, 5, 5], 10)
])
def test_all(nums, out):
    test_sol = Solution()
    assert test_sol.countCompleteSubarrays(nums) == out
