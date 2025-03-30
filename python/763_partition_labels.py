import pytest
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}
        for char_idx in range(len(s)):
            if s[char_idx] not in intervals:
                intervals[s[char_idx]] = [char_idx, None]
            intervals[s[char_idx]][1] = char_idx

        merged_intervals = []
        intervals = list(intervals.values())
        last_interval = intervals.pop(0)
        for start, end in intervals:
            if start < last_interval[1]:
                last_interval[1] = max(end, last_interval[1])
            else:
                merged_intervals.append(last_interval)
                last_interval = [start, end]
        if len(merged_intervals) == 0 or last_interval != merged_intervals[-1]:
            merged_intervals.append(last_interval)

        return [(end - start + 1) for start, end in merged_intervals]


@pytest.mark.parametrize('s, out', [
    ('ababcbacadefegdehijhklij', [9, 7, 8]),
    ('eccbbbbdec', [10])
])
def test_all(s, out):
    test_sol = Solution()
    assert test_sol.partitionLabels(s) == out
