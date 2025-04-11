import pytest


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        while low <= high:
            num = str(low)
            num_len = len(num)
            if num_len % 2 == 1:
                low = 10 ** num_len
                continue
            split_sum = 0
            for i in range(num_len // 2):
                split_sum += int(num[i]) - int(num[- i - 1])
            if split_sum == 0:
                count += 1
            low += 1
        return count


@pytest.mark.parametrize('low, high, out', [
    (1, 100, 9),
    (1200, 1230, 4),
])
def test_all(low, high, out):
    test_sol = Solution()
    assert test_sol.countSymmetricIntegers(low, high) == out
